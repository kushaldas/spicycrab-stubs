"""Target Python shape for tunnelbana nameid microservice codegen."""

from spicycrab.types import Some
from spicycrab_tunnelbana_core import Context, Error, InternalData, MicroService, Result

NAMEID_PERSISTENT: str = "urn:oasis:names:tc:SAML:2.0:nameid-format:persistent"


class NameId(MicroService):
    name: str

    def __init__(self, name: str) -> None:
        self.name = name

    async def process_request(self, ctx: Context, data: InternalData) -> Result[InternalData, Error]:
        ctx.state.set_str(self.name, "subject_type", NAMEID_PERSISTENT)
        return Result.Ok(data)

    async def process_response(self, ctx: Context, data: InternalData) -> Result[InternalData, Error]:
        pairwise = data.attr_first("pairwise-id")
        if pairwise is None:
            return Result.Err(Error.Authn("No pairwise ID to use as persistent NameID"))
        data.subject_id = Some(pairwise.split("@")[0].to_string())
        return Result.Ok(data)
