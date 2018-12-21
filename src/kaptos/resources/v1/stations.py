"""Monitoring stations."""

import roax.schema as s

from .. import KaptosResource
from roax.resource import operation


_schema = s.dict(
    description = "Monitoring station.",
    properties = {
        "id": s.uuid(
            description = "Identifies the station.",
        ),
        "name": s.str(
            description = "Station name.",
        ),
        "description": s.str(
            description = "Description of the station.",
        ),
        "owner_id": s.uuid(
            description = "Identifies the user who controls the station.",
        ),
    },
    required = "name,description,owner_id",
)

class Stations(KaptosResource):
    """TODO: Description."""

    schema = _schema

    def __init__(self):
        super().__init__(name="stations")

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
