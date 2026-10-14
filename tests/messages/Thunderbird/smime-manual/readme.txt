Files in this directory were manually crafted.

Most of them are now refreshed automatically after a test-data refresh (see the
"Automatic refresh" section below); the rest still have to be updated by hand
using the per-file instructions. The manual instructions are kept for reference.


Automatic refresh
=================

mailnews/test/data/smime/local-gen.sh (function update_smime_manual) refreshes
these files after the S/MIME certificates/messages have been regenerated:

  alice.env.mixed.dsig.SHA256.multipart.eml
  alice.dsig.SHA256.multipart.env.dsig.eml
  outer-smime-bad-sig-inner-smime-enc.eml
  outer-smime-bad-sig-inner-smime-enc-sig.eml

For each, it edits the file in place and replaces only:
  - the Date: header, and
  - the inner enveloped-data base64 payload (the first base64 block),
The trailing outer signature block is intentionally left untouched.


Per-file construction
=====================

File alice.env.mixed.dsig.SHA256.multipart.eml
(auto-refreshed by local-gen.sh)
was created by taking file alice.env.dsig.SHA256.multipart.eml as input,
but the inner encrypted block was wrapped in another layer.
That layer was taken from file mailnews/test/data/multipart-message-1.eml
(As a result, the signature doesn't match the data, but that doesn't
matter for this test.)
The automatic refresh replaces the inner enveloped block (with the block from
alice.env.dsig.SHA256.multipart.eml) and the Date, keeping the added wrapper
layer. The block is kept decryptable with the current key on purpose: the test
checks that this wrapped encryption layer is NOT decrypted, which is only
meaningful if decryption would otherwise succeed.


alice.dsig.SHA256.multipart.env.dsig.eml
(auto-refreshed by local-gen.sh)
was created by using the outer structure from alice.env.dsig.SHA256.multipart.eml
and then the inner encrypted block was replaced with the encrypted
block from alice.dsig.SHA256.multipart.env.eml


outer-smime-bad-sig-inner-smime-enc.eml
(auto-refreshed by local-gen.sh)
It uses an outer signature block from any another S/MIME signed message,
for the purposes of the test it doesn't matter that the signature
mismatches.
To update this message, replace the inner encrypted block with the
data block from source file alice.env.eml
In addition, also replace the Date: line from that source file.


outer-smime-bad-sig-inner-smime-enc-sig.eml
(auto-refreshed by local-gen.sh)
It uses an outer signature block from any another S/MIME signed message,
for the purposes of the test it doesn't matter that the signature
mismatches.
To update this message, replace the inner encrypted block with the
data block from source file alice.dsig.SHA256.multipart.env.eml
In addition, also replace the Date: line from that source file.
