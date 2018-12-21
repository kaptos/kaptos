"""User sessions with Kaptos server."""

import roax.schema as s

from .. import KaptosResource
from roax.resource import operation


_schema = s.dict(
    description = "Session with Kaptos server.",
    properties = {
        "id": s.uuid(
            description = "Identifies the session.",
        ),
        "type": s.str(
            enum = {"station", "user"},
            description = "Resource type session is for.",
        ),
        "ref": s.uuid(
            description = "Identifies the resource session is for.",
        ),
        "created": s.datetime(
            description = "Date and time session was created.",
        ),
        "expires": s.datetime(
            description = "Date and time session expires.",
        ),
    },
    required = "type,ref,created",
)

class Sessions(KaptosResource):
    """TODO: Description."""

    schema = _schema

    def __init__(self):
        super().__init__(name="sessions")

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
