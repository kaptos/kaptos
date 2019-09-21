"""Monitoring tasks for stations."""

import dataclasses
import kaptos.db
import kaptos.schema as ks
import roax.schema as s

from roax.resource import operation


@dataclasses.dataclass
class Task:
    """Monitoring task."""

    id: s.uuid(description="Identifies the monitoring task.")
    team_id: s.uuid(
        description="Identifies the organization the monitoring task managed under."
    )
    start_time: s.datetime(
        description="Date and time (inclusive) that the task is scheduled to begin."
    )
    end_time: s.datetime(
        description="Date and time (inclusive) that the task is scheduled to end."
    )
    frequency: s.int(description="Dial frequency to monitor, in hertz.")
    modulation: ks.modulation(description="Modulation of signals to be processed.")
    bandwidth: s.int(description="Monitoring bandwidth, in hertz.")

    _required = "team_id start_time end_time frequency modulation bandwidth"


schema = s.dataclass(Task)


class Tasks(kaptos.db.TableResource):

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
