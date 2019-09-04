"""Users who own/administer groups, tasks and/or stations."""

import kaptos.db
import roax.schema as s

from roax.resource import operation


schema = s.dict(
    description="User who owns/administers teams, tasks and/or stations.",
    properties={
        "id": s.uuid(description="Identifies the user."),
        "email": s.str(description="Email address of the user."),
        "password": s.bytes(
            description="Hash of the password for user to authenticate with server."
        ),
        "name": s.str(description="Full name of the user."),
        "call_sign": s.str(description="Call sign of the user."),
        "status": s.str(
            enum={"active", "suspended"}, description="Status of the user."
        ),
        "created": s.datetime(description="Date and time user record was created."),
        "failures": s.list(
            items=s.datetime(),
            description="Date and time of recent consecutive login failures.",
        ),
    },
    required={"email", "name", "status", "created"},
)


class Users(kaptos.db.TableResource):

    name = "users"

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

    # ----- login -----
    @operation(
        type="action",
        params={
            "email": schema.properties["email"],
            "password": schema.properties["password"],
        },
        returns={"token": s.str()},
    )
    def login(self, email, password):
        pass
