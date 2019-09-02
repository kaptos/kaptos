"""Monitoring stations."""

import kaptos.db
import roax.schema as s

from roax.resource import operation


schema = s.dict(
    description="Monitoring station.",
    properties={
        "id": s.uuid(description="Identifies the station."),
        "name": s.str(description="Station name."),
        "description": s.str(description="Description of the station."),
        "owner_id": s.uuid(description="Identifies the user who controls the station."),
    },
    required={"name", "description", "owner_id"},
)


class Stations(kaptos.db.TableResource):

    name = "stations"

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
