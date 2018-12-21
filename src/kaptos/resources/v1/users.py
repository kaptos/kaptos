"""Users who own/administer groups, tasks and/or stations."""

import roax.schema as s

from .. import KaptosResource
from roax.memory import MemoryResource
from roax.resource import operation


_schema = s.dict(
    description = "User who owns/administers groups, tasks and/or stations.",
    properties = {
        "id": s.uuid(
            description = "Identifies the user.",
        ),
        "email": s.str(
            description = "Email address of the user.",
        ),
        "password": s.bytes(
            description = "Hash of the password for user to authenticate with server.",
            required = False,
        ),
        "name": s.str(
            description = "Full name of the user.",
        ),
        "call_sign": s.str(
            description = "Call sign of the user.",
            required = False,
        ),
        "code": s.str(
            description = "Password reset confirmation code sent to user.",
        ),
        "status": s.str(
            enum = {"active", "suspended"},
            description = "Status of the user.",
        ),
        "created": s.datetime(
            description = "Date and time user record was created.",
        ),
        "failures": s.list(
            items = s.datetime(),
            description = "Date and time of recent consecutive login failures.",
        ),
    },
    required = "email,name,status,created",
)

class Users(KaptosResource):
    """TODO: Description."""

    schema = _schema

    def __init__(self):
        super().__init__(name="users", size=1000, ttl=300)

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

    # ----- register -----

    @operation(
        params = _schema.copy({email, password, name, call_sign}).properties,
        returns = {"success": s.bool(), "error": s.str(required=False)}
    )    

    # ----- login -----
    @operation(
        type = "action",
        params = {"email": _schema.properties["email"], "password": _schema.properties["password"]},
        returns = {"token": s.str()},
    )
    def login(self, email, password):
        pass
