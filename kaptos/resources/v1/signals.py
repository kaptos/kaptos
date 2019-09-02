"""Detected signals, computed from station reception reports."""

import kaptos.db
import roax.geo
import roax.schema as s

from roax.resource import operation


schema = s.dict(
    description="Detected signal, computed from station reception reports.",
    properties={
        "id": s.uuid(description="Identifies the signal."),
        "task_id": s.uuid(description="Identifies the task that signal is for."),
        "report_ids": s.set(
            description="Station receiption reports of the signal.", items=s.uuid()
        ),
        "time": s.datetime(description="Date and time of the signal."),
        "duration": s.int(description="Duration of signal, in seconds.", minimum=1),
        "location": roax.geo.Point(
            description="Computed location of the transmitting station."
        ),
        "cep": s.int(description="Circle error probable of location, in metres."),
        "recording_id": s.uuid(description="Identifies the recording of the signal."),
    },
    required={
        "task_id",
        "report_ids",
        "time",
        "duration",
        "location",
        "cep",
        " recording_id",
    },
)


class Signals(kaptos.db.TableResource):

    name = "signals"

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
