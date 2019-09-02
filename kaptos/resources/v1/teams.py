"""Teams of users and monitoring tasks within a geographic region."""

import kaptos.db
import roax.geo
import roax.schema as s

from roax.resource import operation


schema = s.dict(
    description="Team of users and monitoring tasks within a geographic region.",
    properties={
        "id": s.uuid(description="Identifies the team."),
        "name": s.str(description="Name of the team."),
        "description": s.str(description="Description of the team."),
        "area": roax.geo.Polygon(
            description="Area from which signal reports will be accepted.", max_rings=1
        ),
        "visibility": s.str(
            description="Organization visibility.", enum={"public", "private"}
        ),
    },
    required={"name", "description", "area", "visibility"},
)


class Teams(kaptos.db.TableResource):

    name = "teams"

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
