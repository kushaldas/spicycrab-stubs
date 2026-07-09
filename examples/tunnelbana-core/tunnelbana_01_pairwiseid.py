"""Target Python shape for tunnelbana pairwiseid microservice codegen."""

from spicycrab_tunnelbana_core import Context, Error, InternalData, MicroService, Result


class PairwiseId(MicroService):
    name: str
    pairwise_salt: str

    def __init__(self, name: str, pairwise_salt: str) -> None:
        self.name = name
        self.pairwise_salt = pairwise_salt

    async def process_response(self, ctx: Context, data: InternalData) -> Result[InternalData, Error]:
        subject_id = data.attr_first("subject-id")
        if subject_id is None:
            return Result.Err(Error.Authn("No subject-id attribute found"))
        # The current spicycrab pilot should replace this helper section with
        # the handwritten Rust HMAC-SHA256 implementation target.
        data.set_attr("pairwise-id", subject_id)
        return Result.Ok(data)

