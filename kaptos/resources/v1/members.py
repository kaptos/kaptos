"""User memberships in teams."""

import kaptos.db
import roax.schema as s

from roax.resource import operation


schema = s.dict(
    description="User membership in a team.",
    properties={
        "id": s.uuid(description="Identifies the membership."),
        "team_id": s.uuid(description="Identifies the team."),
        "user_id": s.uuid(description="Identifies the user."),
        "status": s.str(
            enum={"active", "suspended", "requested", "denied"},
            description="Status of user's group membership.",
        ),
        "roles": s.set(
            items=s.str(enum={"read", "submit", "admin", "owner"}),
            description="User role(s) in team.",
        ),
    },
    required={"team_id", "user_id", "status", "roles"},
)


class Members(kaptos.db.TableResource):

    name = "members"

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
