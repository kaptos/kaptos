"""Detected transmissions, computed from station reception reports."""

import kaptos.schema as ks
import roax.schema as s

from .. import KaptosResource
from roax.resource import operation


_schema = s.dict(
    description = "Detected transmission, corroborated by station signal reports.",
    properties = {
        "id": s.uuid(
            description = "Identifies the transmission.",
        ),
        "task_id": s.uuid(
            description = "Identifies the task that transmission is for.",
        ),
        "report_ids": s.set(
            items = s.uuid(),
            description = "Station receiption reports of the signal.",
        },
        "time": s.datetime(
            description = "Date and time of the transmission.",
        ),
        "duration": s.int(
            description = "Duration of transmission, in seconds.",
            min_value = 1,
        ),
        "location": ks.geojson_point(
            description = "Computed location of the transmitting station.",
        ),
        "cep": s.int(
            description = "Circle error probable of location, in metres.",
        ),
        "recording_id": s.uuid(
            description = "Identifies the recording of the transmission.",
        )
    },
    required = "task_id,report_ids,time,duration,location,cep,recording_id",
)

class Transmissions(KaptosResource):

    schema = _schema

    def __init__(self):
        super().__init__(name="transmissions")

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
