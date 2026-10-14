#!/bin/bash

set -e

# This script creates additional S/MIME test files.
# It's called automatically by generate.sh.
# However, it can also be called directly, if the test data from NSS
# is still sufficiently fresh, and only the local test files need to
# be updated, e.g. when adding new tests.

if [ -n "$NSS_LIB_PATH" ]
then
  export LD_LIBRARY_PATH=${NSS_LIB_PATH}:$LD_LIBRARY_PATH
  export SHLIB_PATH=${NSS_LIB_PATH}:$SHLIB_PATH
  export LIBPATH=${NSS_LIB_PATH}:$LIBPATH
  export DYLD_LIBRARY_PATH=${NSS_LIB_PATH}:$DYLD_LIBRARY_PATH
fi

if ! test -e generate.sh || ! test -e local-gen.sh
then
  echo "you must run this script from inside the directory that contains local-gen.sh and generate.sh"
  exit
fi

if ! hash certutil || ! hash pk12util || ! hash atob || ! hash btoa
then
  echo "Required NSS utilities cannot be executed. Add \$OBJDIR/dist/bin of a local Thunderbird build to both the PATH and (platform specific) library path environment variable (e.g. LD_LIBRARY_PATH or DYLD_LIBRARY_PATH)."
  exit
fi

MILLDIR="$(pwd)/../../../../mail/test/browser/smime/data"

# When executing mochitests in the CI environment, the files from this
# directory aren't available. Copy all files that mochitests requires to
# the mochitests directory.
cp -rv Alice.p12 Bob.p12 TestCA.pem "$MILLDIR"
cp -rv alice.dsig.SHA256.multipart.env.eml "$MILLDIR"
cp -rv alice.sig.SHA256.opaque.eml "$MILLDIR"
cp -rv alice.sig.SHA256.opaque.env.eml "$MILLDIR"
cp -rv alice.html.sig.SHA256.opaque.eml "$MILLDIR"
cp -rv alice.html.sig.SHA256.opaque.env.eml "$MILLDIR"
cp -rv alice.env.eml "$MILLDIR"
cp -rv alice.remoteimage.env.eml "$MILLDIR"

TMPDIR="./tmp-local"
mkdir $TMPDIR

BOUNDARY="--------BOUNDARY"

EMAILDATE=$(date --rfc-email --utc)

MSGHEADER="MIME-Version: 1.0
Date: ${EMAILDATE}
From: Alice <alice@example.com>
To: Bob <bob@example.com>
Subject: a message
Content-Type: multipart/alternative; boundary=\"${BOUNDARY}\"

"

ENVHEADER="Content-Type: application/pkcs7-mime; smime-type=enveloped-data
Content-Transfer-Encoding: base64

"

certutil -d $TMPDIR -N --empty-password
pk12util -d $TMPDIR -i Alice.p12 -W nss
pk12util -d $TMPDIR -i Bob.p12 -W nss
certutil -d $TMPDIR -M -n TestCA -t C,C,

INPUT="Content-type: text/plain

SECRET-TEXT the attacker wants to steal
"
echo "$INPUT" | cmsutil -d $TMPDIR -E -r bob@example.com | btoa > $TMPDIR/prey.b64

INPUT="Content-type: text/html

<pre>Please reply to this harmless looking message</pre><style>.moz-text-plain, .moz-quote-pre, fieldset {display: none;}</style>"
echo "$INPUT" | cmsutil -d $TMPDIR -E -r bob@example.com | btoa > $TMPDIR/bait.b64

MSG=$TMPDIR/msg.eml

{
  echo -n "$MSGHEADER"
  echo "--$BOUNDARY"
  echo -n "$ENVHEADER"
  cat $TMPDIR/bait.b64
  echo "--$BOUNDARY"
  echo -n "$ENVHEADER"
  cat $TMPDIR/prey.b64
  echo "--$BOUNDARY"
} > $MSG

mv $MSG "$MILLDIR/multipart-alternative.eml"

# Create a message with a mismatching message date (use a later time,
# because the test certificates aren't valid at earlier times).

GOOD_DATE=$(grep ^Date "alice.dsig.SHA256.multipart.eml" | sed 's/^Date: //')
FUTURE_DATE=$(date --utc --rfc-email --date="${GOOD_DATE} + 6 hours")
sed "s/^Date: .*$/Date: ${FUTURE_DATE}/" "alice.dsig.SHA256.multipart.eml" > "alice.future.dsig.SHA256.multipart.eml"

# Refresh the hand-crafted files in ../smime-manual (see its readme.txt). Their
# structure is stable across a data refresh; only the Date header and the inner
# enveloped payload need to be replaced with the current values from a generated
# source message. The trailing (intentionally mismatched, and ignored) outer
# signature block is left untouched.
#
# $1: file name in ../smime-manual
# $2: generated source message (a top-level enveloped message) providing the
#     fresh Date and enveloped payload.
update_smime_manual() {
  manual="../smime-manual/$1"
  src="$2"

  [ -f "$manual" ] || { echo "update_smime_manual: no such file: $manual" >&2; exit 1; }
  [ -f "$src" ] || { echo "update_smime_manual: no such source: $src" >&2; exit 1; }

  newdate=$(grep -m1 '^Date:' "$src" | sed 's/^Date: //; s/\r$//')
  [ -n "$newdate" ] || {
    echo "update_smime_manual: no Date: header in source $src" >&2; exit 1; }

  # The fresh enveloped payload is the base64 block of the source's first
  # enveloped-data part (a source may also contain a later signature block,
  # which must not be picked up).
  awk '
    { l = $0; sub(/\r$/, "", l) }
    state == 0 && l ~ /smime-type=enveloped-data/ { state = 1; next }
    state == 1 && l == "" { state = 2; next }
    state == 2 {
      if (l ~ /^[A-Za-z0-9+\/]+={0,2}$/) { print; next }
      exit
    }
  ' "$src" > "$TMPDIR/payload.b64"
  [ -s "$TMPDIR/payload.b64" ] || {
    echo "update_smime_manual: no enveloped-data payload found in source $src" >&2
    exit 1; }

  # Locate, in the manual file, the blank line ending the enveloped-data part
  # headers and the last line of its base64 payload. Only the first base64 run
  # (the enveloped payload) is considered; the later pkcs7-signature block is
  # left alone.
  headend=""; payend=""
  # Don't let a non-match trip set -e here; it is reported explicitly below.
  read -r headend payend < <(awk '
    { l = $0; sub(/\r$/, "", l) }
    state == 0 && l ~ /smime-type=enveloped-data/ { state = 1; next }
    state == 1 && l == "" { headend = NR; state = 2; next }
    state == 2 {
      if (l ~ /^[A-Za-z0-9+\/]+={0,2}$/) { payend = NR; next }
      print headend, payend; exit
    }
  ' "$manual") || true

  valid=1
  case "$headend" in '' | *[!0-9]*) valid=0 ;; esac
  case "$payend" in '' | *[!0-9]*) valid=0 ;; esac
  if [ "$valid" = 0 ] || [ "$payend" -lt "$headend" ]; then
    echo "update_smime_manual: could not locate an enveloped-data block in $manual (unexpected structure)" >&2
    exit 1
  fi

  {
    sed -n "1,${headend}p" "$manual" | sed "s/^Date: .*/Date: ${newdate}\r/"
    cat "$TMPDIR/payload.b64"
    sed -n "$((payend + 1)),\$p" "$manual"
  } > "$manual.tmp"
  mv "$manual.tmp" "$manual"
  echo "updated $manual"
}

update_smime_manual alice.dsig.SHA256.multipart.env.dsig.eml \
  alice.dsig.SHA256.multipart.env.eml
update_smime_manual outer-smime-bad-sig-inner-smime-enc-sig.eml \
  alice.dsig.SHA256.multipart.env.eml
update_smime_manual outer-smime-bad-sig-inner-smime-enc.eml \
  alice.env.eml
# The encryption layer here must stay decryptable with the current key so the
# test genuinely exercises the code refusing to decrypt this wrapped layer
# (a stale, undecryptable blob would pass trivially).
update_smime_manual alice.env.mixed.dsig.SHA256.multipart.eml \
  alice.env.dsig.SHA256.multipart.eml

# Wrap the clear-signed message in a multipart/mixed part and append an
# unsigned footer, like mailing list software does. The signed part is
# copied unmodified, its signature remains valid.
# The signed part is at MIME part number 1.1, unless an unsigned header
# part is added in front of it, then it is at 1.2.
# $1: output file, $2: if "header", add an unsigned part before the
# signed part.

MIXED_BOUNDARY="============MIXEDBOUNDARY=="
MIXED_DATE=$(printf '%s' "${GOOD_DATE}" | tr -d '\r')
MIXED_SIGNED_CT=$(grep -i '^Content-Type: multipart/signed' "alice.dsig.SHA256.multipart.eml" | tr -d '\r')

wrap_signed_in_mixed() {
  {
    printf 'MIME-Version: 1.0\r\n'
    printf 'Date: %s\r\n' "${MIXED_DATE}"
    printf 'From: Alice@example.com\r\n'
    printf 'To: test-list@example.com\r\n'
    printf 'Subject: [test-list] clear-signed sig.SHA256 wrapped in multipart/mixed\r\n'
    printf 'Content-Type: multipart/mixed; boundary="%s"\r\n' "${MIXED_BOUNDARY}"
    printf '\r\n'
    if [ "$2" = "header" ]
    then
      printf -- '--%s\r\n' "${MIXED_BOUNDARY}"
      printf 'Content-Type: text/plain; charset="us-ascii"\r\n'
      printf 'Content-Transfer-Encoding: 7bit\r\n'
      printf 'Content-Description: Mailing list header\r\n'
      printf '\r\n'
      printf 'Welcome to the test-list mailing list.\r\n'
      printf '\r\n'
    fi
    printf -- '--%s\r\n' "${MIXED_BOUNDARY}"
    printf '%s\r\n' "${MIXED_SIGNED_CT}"
    printf '\r\n'
    # Everything after the header block, that is the complete signed part.
    sed '1,/^\r*$/d' "alice.dsig.SHA256.multipart.eml"
    printf -- '--%s\r\n' "${MIXED_BOUNDARY}"
    printf 'Content-Type: text/plain; charset="us-ascii"\r\n'
    printf 'Content-Transfer-Encoding: 7bit\r\n'
    printf 'Content-Description: Mailing list footer\r\n'
    printf '\r\n'
    printf 'test-list mailing list -- test-list@example.com\r\n'
    printf '\r\n'
    printf -- '--%s--\r\n' "${MIXED_BOUNDARY}"
  } > "$1"
}

wrap_signed_in_mixed "$MILLDIR/alice.dsig.SHA256.multipart.in.mixed.eml"
wrap_signed_in_mixed "$MILLDIR/alice.dsig.SHA256.multipart.in.mixed.with.header.eml" header

rm -rf $TMPDIR
