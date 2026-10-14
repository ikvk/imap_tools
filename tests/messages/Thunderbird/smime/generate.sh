#!/bin/bash

set -e

# This script creates updated data for automated S/MIME tests.
# It will do a local build of NSS, execute parts of the NSS test suite,
# and copy data created by it to the local source tree.

if ! test -e generate.sh || ! test -e local-gen.sh
then
  echo "you must run this script from inside the directory that contains generate.sh and local-gen.sh"
  exit
fi

mkdir nssbuild
pushd nssbuild

cp -riv ../../../../../../security/nss nss
cp -riv ../../../../../../nsprpub nspr

export USE_64=1
cd nss
make nss_build_all

export NSS_CYCLES=sharedb
export NSS_TESTS=smime
cd tests
HOST=localhost DOMSUF=localdomain ./all.sh

popd
cp -v nssbuild/tests_results/security/localhost.1/sharedb/smime/tb/*.eml .
cp -v nssbuild/tests_results/security/localhost.1/sharedb/smime/tb/*.p12 .
cp -v nssbuild/tests_results/security/localhost.1/sharedb/smime/tb/*.pem .

CWD=$(pwd)

EXPIRATION_INFO_FILE="$CWD/expiration.txt"
ALICE_DIR="$CWD/nssbuild/tests_results/security/localhost.1/sharedb/alicedir"

export DIST="$CWD/nssbuild/dist/"

pushd nssbuild/nss/tests/common
OBJDIR=$(make objdir_name)
export OBJDIR
popd

# PATH logic copied from nss/tests/common/init.sh
if [ "${OS_ARCH}" = "WINNT" ] && [ "$OS_NAME" != "CYGWIN_NT" ] && [ "$OS_NAME" != "MINGW32_NT" ]; then
    PATH=.\;${DIST}/${OBJDIR}/bin\;${DIST}/${OBJDIR}/lib\;$PATH
    PATH=$(perl ../path_uniq -d ';' "$PATH")
elif [ "${OS_ARCH}" = "Android" ]; then
    # android doesn't have perl, skip the uniq step
    PATH=.:${DIST}/${OBJDIR}/bin:${DIST}/${OBJDIR}/lib:$PATH
else
    PATH=.:${DIST}/${OBJDIR}/bin:${DIST}/${OBJDIR}/lib:/bin:/usr/bin:$PATH
    # added /bin and /usr/bin in the beginning so a local perl will
    # be used
    PATH=$(perl nssbuild/nss/tests/path_uniq -d ':' "$PATH")
fi

export PATH
export LD_LIBRARY_PATH=${DIST}/${OBJDIR}/lib:$LD_LIBRARY_PATH
export SHLIB_PATH=${DIST}/${OBJDIR}/lib:$SHLIB_PATH
export LIBPATH=${DIST}/${OBJDIR}/lib:$LIBPATH
export DYLD_LIBRARY_PATH=${DIST}/${OBJDIR}/lib:$DYLD_LIBRARY_PATH

certutil -d "${ALICE_DIR}" -L -n Alice |grep -i "Not After" | \
  sed 's/^.*: //' > "${EXPIRATION_INFO_FILE}"

# exporting DYLD_LIBRARY_PATH to a subprocess doesn't work on recent OSX
export NSS_LIB_PATH=${DIST}/${OBJDIR}/lib

# Now refresh Thunderbird's local test data that is based on the NSS
# test suite data.
./local-gen.sh

echo "Done. Will remove the NSS build/test tree in 20 seconds."
sleep 20
rm -rf nssbuild
