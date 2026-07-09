"""Target Python shape for tunnelbana ACCR microservice codegen."""

from spicycrab_tunnelbana_core import Context, Error, InternalData, MicroService, Result


class Accr(MicroService):
    name: str
    supported_accr_sorted_by_prio: list[str]

    def __init__(self, name: str, supported_accr_sorted_by_prio: list[str]) -> None:
        self.name = name
        self.supported_accr_sorted_by_prio = supported_accr_sorted_by_prio

    async def process_response(self, ctx: Context, data: InternalData) -> Result[InternalData, Error]:
        requested = ctx.state.get_value(self.name, "requested_accr")
        if requested is None:
            return Result.Ok(data)
        return Result.Ok(data)

