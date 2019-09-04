"""Monitoring tasks for stations."""

import kaptos.db
import kaptos.schema as ks
import roax.schema as s

from roax.resource import operation


schema = s.dict(
    description="Monitoring task.",
    properties={
        "id": s.uuid(description="Identifies the monitoring task."),
        "team_id": s.uuid(
            description="Identifies the organization the monitoring task managed under."
        ),
        "start_time": s.datetime(
            description="Date and time (inclusive) that the task is scheduled to begin."
        ),
        "end_time": s.datetime(
            description="Date and time (inclusive) that the task is scheduled to end."
        ),
        "frequency": s.int(description="Dial frequency to monitor, in hertz."),
        "modulation": ks.modulation(
            description="Modulation of signals to be processed."
        ),
        "bandwidth": s.int(description="Monitoring bandwidth, in hertz."),
    },
    required={
        "team_id",
        "start_time",
        "end_time",
        "frequency",
        "modulation",
        "bandwidth",
    },
)


class Tasks(kaptos.db.TableResource):

    name = "tasks"

    schema = schema

    # ---- create ------
    @operation(
        params={"_body": schema}, returns=s.dict({"id": schema.properties["id"]})
    )
    def create(self, _body):
        return super().create(_body)

    # ----- read ------
    @operation(params={"id": schema.properties["id"]}, returns=schema)
    def read(self, id):
        return super().read(id)

    # ----- update ------
    @operation(params={"id": schema.properties["id"], "_body": schema}, returns=None)
    def update(self, id, _body):
        return super().update(id, _body)

    # ----- delete ------
    @operation(params={"id": schema.properties["id"]}, returns=None)
    def delete(self, id):
        return super().delete(id)
