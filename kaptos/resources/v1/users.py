"""Users who own/administer groups, tasks and/or stations."""

import dataclasses
import kaptos.db
import roax.schema as s

from roax.resource import operation


@dataclasses.dataclass
class User:
    """User who owns/administers teams, tasks and/or stations."""

    id: s.uuid(description="Identifies the user.")
    email: s.str(description="Email address of the user.")
    password: s.bytes(
        description="Hash of the password for user to authenticate with server."
    )
    name: s.str(description="Full name of the user.")
    call_sign: s.str(description="Call sign of the user.")
    status: s.str(enum={"active", "suspended"}, description="Status of the user.")
    created: s.datetime(description="Date and time user record was created.")
    failures: s.list(
        items=s.datetime(),
        description="Date and time of recent consecutive login failures.",
    )

    _required = "email name status created"


schema = s.dataclass(User)


class Users(kaptos.db.TableResource):

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

    @operation(type="action")
    def login(
        self, email: schema.attrs.email, password: schema.attrs.password
    ) -> s.dict({"token": s.str()}):
        pass
