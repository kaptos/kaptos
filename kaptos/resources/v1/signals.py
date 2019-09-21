"""Detected signals, computed from station reception reports."""

import dataclasses
import kaptos.db
import roax.geo
import roax.schema as s

from roax.resource import operation


@dataclasses.dataclass
class Signal:
    """Detected signal, computed from station reception reports."""

    id: s.uuid(description="Identifies signal.")
    task_id: s.uuid(description="Identifies task that signal is for.")
    report_ids: s.set(
        description="Station receiption reports of signal.", items=s.uuid()
    )
    time: s.datetime(description="Date and time of signal.")
    duration: s.int(description="Duration of signal, in seconds.", min=1)
    location: roax.geo.Point(description="Computed location of transmitting station.")
    cep: s.int(description="Circle error probable of location, in metres.")

    _required = "task_id report_ids time duration location cep"


schema = s.dataclass(Signal)


class Signals(kaptos.db.TableResource):

    schema = schema

    @operation
    def create(self, _body: schema) -> s.dict({"id": schema.attrs.id}):
        return super().create(_body)

    @operation
    def read(self, id: schema.attrs.id) -> schema:
        return super().read(id)

    @operation
    def update(self, id: schema.attrs.id, _body: schema) -> None:
        return super().update(id, _body)

    @operation
    def delete(self, id: schema.attrs.id) -> None:
        return super().delete(id)
