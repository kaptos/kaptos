"""Monitoring tasks for stations."""

import kaptos.schema as ks
import roax.schema as

from .. import KaptosResource
from roax.resource import operation


_schema = s.dict(
    description = "Monitoring task stations.",
    properties = {
        "id": s.uuid(
            description = "Identifies the monitoring task.",
        ),
        "organization_id": s.uuid(
            description = "Identifies the organization the monitoring task is a part of.",
        ),
        "start_time": s.datetime(
            description = "Date and time (inclusive) that the task is scheduled to begin.",
        ),
        "end_time": s.datetime(
            description = "Date and time (inclusive) that the task is scheduled to end.",
        ),
        "frequency": s.int(
            description = "Dial frequency to monitor, in hertz.",
        ),
        "modulation": ks.modulation(
            description = "Modulation of signals to be processed.",
        ),
        "filter_width": s.int(
            description = "Filter width, in hertz.",
        ),
    },
    required = "organization_id,start_time,end_time,frequency,modulation,filter_width",
)

class Tasks(KaptosResource):

    schema = _schema

    def __init__(self):
        super().__init__(name="tasks")

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
