"""Target Python shape for tunnelbana metrics microservice codegen."""

from spicycrab_tunnelbana_core import Context, Error, InternalData, MicroService, Result


class Metrics(MicroService):
    name: str

    def __init__(self, name: str) -> None:
        self.name = name

    async def process_response(self, ctx: Context, data: InternalData) -> Result[InternalData, Error]:
        requester = data.requester
        if requester is None:
            return Result.Ok(data)
        return Result.Ok(data)

