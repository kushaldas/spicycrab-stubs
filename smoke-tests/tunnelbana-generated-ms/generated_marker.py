"""Generated microservice smoke test source."""

from spicycrab_tunnelbana_core import Context, Error, InternalData, MicroService, Result


class GeneratedMarker(MicroService):
    name: str
    marker_value: str

    def __init__(self, name: str, marker_value: str) -> None:
        self.name = name
        self.marker_value = marker_value

    async def process_request(self, ctx: Context, data: InternalData) -> Result[InternalData, Error]:
        ctx.state.set_str(self.name, "request_seen", "yes")
        return Result.Ok(data)

    async def process_response(self, ctx: Context, data: InternalData) -> Result[InternalData, Error]:
        data.set_attr("generated-marker", self.marker_value)
        return Result.Ok(data)
