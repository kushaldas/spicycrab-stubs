"""Target Python shape for tunnelbana pairwiseid microservice codegen."""

from spicycrab_tunnelbana_core import (
    Context,
    Error,
    InternalData,
    MicroService,
    Result,
    derive_pairwise_id,
)


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
        requester = data.requester
        if requester is None:
            anonymous_pairwise = derive_pairwise_id(self.pairwise_salt, "", subject_id)
            data.set_attr("pairwise-id", anonymous_pairwise)
            return Result.Ok(data)
        pairwise = derive_pairwise_id(self.pairwise_salt, requester, subject_id)
        data.set_attr("pairwise-id", pairwise)
        return Result.Ok(data)
