"""Teams of users and monitoring tasks within a geographic region."""

import kaptos.schema as ks
import roax.schema as

from .. import KaptosResource
from roax.resource import operation


_schema = s.dict(
    description = "Team of users and monitoring tasks within a geographic region.",
    properties = {
        "id": s.uuid(
            description = "Identifies the team.",
        ),
        "name" = s.str(
            description = "Name of the team.",
        ),
        "description" = s.str(
            description = "Description of the team.",
        ),
        "area": ks.geojson_polygon(
            max_rings = 1,
            description = "Area from which signal reports will be accepted.",
        ),
        "visibility": s.str(
            enum = {"public", "private"}
            description = "Team visibility.",
        ),
    },
    required = "name,description,area,visibility",
)


class Teams(KaptosResource):
    """TODO: Description."""

    schema = _schema

    def __init__(self):
        super().__init__("teams")

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
