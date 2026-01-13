"""Test passthrough Rust attributes via # #[...] comments."""

from dataclasses import dataclass


# #[derive(Serialize, Deserialize, Debug, Clone)]
# #[serde(rename_all = "camelCase")]
@dataclass
class EntityDetails:
    """An entity in the federation."""
    entity_id: str
    entity_type: str
    has_trustmark: bool


# #[derive(Debug, Clone, PartialEq)]
@dataclass
class ResolveParams:
    """Query parameters for resolve endpoint."""
    sub: str
    anchor: str


# #[inline]
def add(a: int, b: int) -> int:
    """Add two numbers."""
    return a + b


# #[get("/.well-known/openid-federation")]
async def openid_federation() -> str:
    """OpenID Federation endpoint."""
    return "entity-statement-jwt"


# #[tokio::test]
async def test_something() -> None:
    """A test function."""
    result: int = add(1, 2)
    print(result)


def main() -> None:
    """Main entry point."""
    entity: EntityDetails = EntityDetails(
        entity_id="https://example.com",
        entity_type="openid_relying_party",
        has_trustmark=True
    )
    print(entity.entity_id)
