"""Python stubs for the tunnelbana-plugins Rust crate."""

from __future__ import annotations

from spicycrab_tunnelbana_core import Backend, BuildContext, Error, Frontend, MicroService, Registry, Result


def register_all(registry: Registry) -> None: ...


class OidcFrontend:
    @staticmethod
    def build(bx: BuildContext) -> Result[Frontend, Error]: ...


class FederationFrontend:
    @staticmethod
    def build(bx: BuildContext) -> Result[Frontend, Error]: ...


class Saml2Frontend:
    @staticmethod
    def build(bx: BuildContext) -> Result[Frontend, Error]: ...


class OidcBackend:
    @staticmethod
    def build(bx: BuildContext) -> Result[Backend, Error]: ...


class FederationBackend:
    @staticmethod
    def build(bx: BuildContext) -> Result[Backend, Error]: ...


class Saml2Backend:
    @staticmethod
    def build(bx: BuildContext) -> Result[Backend, Error]: ...


class StaticAttributes:
    @staticmethod
    def build(bx: BuildContext) -> Result[MicroService, Error]: ...


class FilterAttributes:
    @staticmethod
    def build(bx: BuildContext) -> Result[MicroService, Error]: ...


class CustomRouting:
    @staticmethod
    def build(bx: BuildContext) -> Result[MicroService, Error]: ...


class AttributeProcessor:
    @staticmethod
    def build(bx: BuildContext) -> Result[MicroService, Error]: ...


class AttributeAuthorization:
    @staticmethod
    def build(bx: BuildContext) -> Result[MicroService, Error]: ...


class FilterAttributeValues:
    @staticmethod
    def build(bx: BuildContext) -> Result[MicroService, Error]: ...


class RenameAttributes:
    @staticmethod
    def build(bx: BuildContext) -> Result[MicroService, Error]: ...


class AttributeGeneration:
    @staticmethod
    def build(bx: BuildContext) -> Result[MicroService, Error]: ...


class Hasher:
    @staticmethod
    def build(bx: BuildContext) -> Result[MicroService, Error]: ...


class LegacyEptid:
    @staticmethod
    def build(bx: BuildContext) -> Result[MicroService, Error]: ...


class PrimaryIdentifier:
    @staticmethod
    def build(bx: BuildContext) -> Result[MicroService, Error]: ...


class IdpHinting:
    @staticmethod
    def build(bx: BuildContext) -> Result[MicroService, Error]: ...


class CustomLogging:
    @staticmethod
    def build(bx: BuildContext) -> Result[MicroService, Error]: ...


class PairwiseId:
    @staticmethod
    def build(bx: BuildContext) -> Result[MicroService, Error]: ...


class StaticAttributesForVirtualIdp:
    @staticmethod
    def build(bx: BuildContext) -> Result[MicroService, Error]: ...


class NameId:
    @staticmethod
    def build(bx: BuildContext) -> Result[MicroService, Error]: ...


class Accr:
    @staticmethod
    def build(bx: BuildContext) -> Result[MicroService, Error]: ...
