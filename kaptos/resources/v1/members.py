"""User memberships in teams."""

import dataclasses
import kaptos.db
import roax.schema as s

from roax.resource import operation


@dataclasses.dataclass
class Member:
    """User membership in team."""

    id: s.uuid(description="Identifies the membership.")
    team_id: s.uuid(description="Identifies the team.")
    user_id: s.uuid(description="Identifies the user.")
    status: s.str(
        description="Status of user's group membership.",
        enum={"active", "suspended", "requested", "denied"},
    )
    roles: s.set(
        description="User role(s) in team.",
        items=s.str(enum={"read", "submit", "admin", "owner"}),
    )

    _required = "team_id user_id status roles"


schema = s.dataclass(Member)


class Members(kaptos.db.TableResource):

    schema = schema

    @operation
    def create(self, _body: schema) -> s.dict({"id": schema.attrs.id}):
        return super().create(_body)

    @operation
    def read(self, id: schema.attrs.id) -> schema:
        return super().read(id)

    @operation
    def update(self, id: schema.attrs.id, _body: schema) -> None:
        return super().update(id, _body)

    @operation
    def delete(self, id: schema.attrs.id) -> None:
        return super().delete(id)
