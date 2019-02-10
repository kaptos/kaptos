"""User memberships in teams."""

import roax.schema as s

from .. import KaptosResource
from roax.resource import operation


_schema = s.dict(
    description = "User membership in a team.",
    properties = {
        "id": s.uuid(
            description = "Identifies the membership.",
        ),
        "team_id": s.uuid(
            description = "Identifies the team.",
        ),
        "user_id": s.uuid(
            description = "Identifies the user.",
        ),
        "status": s.str(
            enum = {"active", "suspended", "requested", "denied"},
            description = "Status of user's group membership.",
        ),
        "roles": s.set(
            items = s.str(enum = {"read", "submit", "admin", "owner"}),
            description = "User role(s) in team.",
        ),
    },
    required = "team_id,user_id,sttus,roles",
)

class Members(KaptosResource):

    schema = _schema

    def __init__(self):
        super().__init__(name="members")

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
