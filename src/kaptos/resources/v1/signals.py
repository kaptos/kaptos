"""Detected signals, computed from station reception reports."""

import kaptos.schema as ks
import roax.schema as s

from .. import KaptosResource
from roax.resource import operation


_schema = s.dict(
    description = "Detected signal, corroborated by station signal reports.",
    properties = {
        "id": s.uuid(
            description = "Identifies the signal.",
        ),
        "task_id": s.uuid(
            description = "Identifies the task that signal is for.",
        ),
        "report_ids": s.set(
            items = s.uuid(),
            description = "Station receiption reports of the signal.",
        },
        "time": s.datetime(
            description = "Date and time of the signal.",
        ),
        "duration": s.int(
            description = "Duration of signal, in seconds.",
            min_value = 1,
        ),
        "location": ks.geojson_point(
            description = "Computed location of the transmitting station.",
        ),
        "cep": s.int(
            description = "Circle error probable of location, in metres.",
        ),
        "recording_id": s.uuid(
            description = "Identifies the recording of the signal.",
        )
    },
    required = "task_id,report_ids,time,duration,location,cep,recording_id",
)

class Signals(KaptosResource):

    schema = _schema

    def __init__(self):
        super().__init__(name="signals")

    # ---- create ------
    @operation(
        params = {"_body": _schema},
        returns = s.dict({"id": _schema.properties["id"]})
    )
    def create(self, _body):
        return super().create(_body)

    # ----- read ------
    @operation(
        params = {"id": _schema.properties["id"]},
        returns = _schema,
    )
    def read(self, id):
        return super().read(id)

    # ----- update ------
    @operation(
        params = {"id": _schema.properties["id"], "_body": _schema},
        returns = None,
    )
    def update(self, id, _body):
        return super().update(id, _body)

    # ----- delete ------
    @operation(
        params = {"id": _schema.properties["id"]},
        returns = None,
    )
    def delete(self, id):
        return super().delete(id)
