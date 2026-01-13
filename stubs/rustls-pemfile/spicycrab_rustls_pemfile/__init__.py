"""Python stubs for the rustls-pemfile Rust crate.

Install with: cookcrab install rustls-pemfile
"""

from __future__ import annotations

from typing import Self

class Item:
    """The contents of a single recognised block in a PEM file."""
    X509Certificate: "Item"
    SubjectPublicKeyInfo: "Item"
    Pkcs1Key: "Item"
    Pkcs8Key: "Item"
    Sec1Key: "Item"
    Crl: "Item"
    Csr: "Item"

class Error:
    """Errors that may arise when parsing the contents of a PEM file

This differs from [`rustls_pki_types::pem::Error`] because it is `PartialEq`;
it is retained for compatibility."""
    MissingSectionEnd: "Error"
    IllegalSectionStart: "Error"
    Base64Decode: "Error"

    @staticmethod
    def from_(error: Exception) -> "Error": ...

    @staticmethod
    def from_(error: Exception) -> "Error": ...

"""Extract and decode the next PEM section from `input`

- `Ok(None)` is returned if there is no PEM section to read from `input`
- Syntax errors and decoding errors produce a `Err(...)`
- Otherwise each decoded section is returned with a `Ok(Some((Item::..., remainder)))` where
`remainder` is the part of the `input` that follows the returned section"""
def read_one_from_slice(input: object) -> object: ...

"""Extract and decode the next PEM section from `rd`.

- Ok(None) is returned if there is no PEM section read from `rd`.
- Underlying IO errors produce a `Err(...)`
- Otherwise each decoded section is returned with a `Ok(Some(Item::...))`

You can use this function to build an iterator, for example:
`for item in iter::from_fn(|| read_one(rd).transpose()) { ... }`"""
def read_one(rd: BufRead) -> Item | None: ...

"""Extract and return all PEM sections by reading `rd`."""
def read_all(rd: BufRead) -> object: ...

"""Return an iterator over certificates from `rd`.

Filters out any PEM sections that are not certificates and yields errors if a problem
occurs while trying to extract a certificate."""
def certs(rd: BufRead) -> object: ...

"""Return the first private key found in `rd`.

Yields the first PEM section describing a private key (of any type), or an error if a
problem occurs while trying to read PEM sections."""
def private_key(rd: BufRead) -> PrivateKeyDer | None: ...

"""Return the first certificate signing request (CSR) found in `rd`.

Yields the first PEM section describing a certificate signing request, or an error if a
problem occurs while trying to read PEM sections."""
def csr(rd: BufRead) -> CertificateSigningRequestDer | None: ...

"""Return an iterator certificate revocation lists (CRLs) from `rd`.

Filters out any PEM sections that are not CRLs and yields errors if a problem occurs
while trying to extract a CRL."""
def crls(rd: BufRead) -> object: ...

"""Return an iterator over RSA private keys from `rd`.

Filters out any PEM sections that are not RSA private keys and yields errors if a problem
occurs while trying to extract an RSA private key."""
def rsa_private_keys(rd: BufRead) -> object: ...

"""Return an iterator over PKCS8-encoded private keys from `rd`.

Filters out any PEM sections that are not PKCS8-encoded private keys and yields errors if a
problem occurs while trying to extract an RSA private key."""
def pkcs8_private_keys(rd: BufRead) -> object: ...

"""Return an iterator over SEC1-encoded EC private keys from `rd`.

Filters out any PEM sections that are not SEC1-encoded EC private keys and yields errors if a
problem occurs while trying to extract a SEC1-encoded EC private key."""
def ec_private_keys(rd: BufRead) -> object: ...

"""Return an iterator over SPKI-encoded keys from `rd`.

Filters out any PEM sections that are not SPKI-encoded public keys and yields errors if a
problem occurs while trying to extract a SPKI-encoded public key."""
def public_keys(rd: BufRead) -> object: ...

__all__: list[str] = ["read_one_from_slice", "read_one", "read_all", "certs", "private_key", "csr", "crls", "rsa_private_keys", "pkcs8_private_keys", "ec_private_keys", "public_keys", "Item", "Error"]
