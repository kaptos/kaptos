"""User sessions with Kaptos server."""

import kaptos.db
import roax.schema as s

from roax.resource import operation


schema = s.dict(
    description="Session with Kaptos service.",
    properties={
        "id": s.uuid(description="Identifies the session."),
        "type": s.str(
            enum={"station", "user"}, description="Resource type session is for."
        ),
        "ref": s.uuid(description="Identifies the station or user session is for."),
        "created": s.datetime(description="Date and time session was created."),
        "expires": s.datetime(description="Date and time session expires."),
    },
    required={"type", "ref", "created"},
)


class Sessions(kaptos.db.TableResource):

    name = "sessions"

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
