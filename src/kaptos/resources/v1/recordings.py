"""Recordings of received signals."""

import roax.schema as s

from .. import KaptosResource
from roax.resource import operation


_schema = s.dict(
    description = "Recording of a received signal.",
    properties = {
        "id": s.uuid(
            description = "Identifies the recording."
            required = False,
        ),
        "user_id": s.uuid(
            description = "User who uploaded the recording.",
        ),
        "url": s.bytes(
            content_type = "audio/opus",
            description = "Recording content.",
        ),
    },
    required = "user_id,content",
)

class Recordings(KaptosResource):
    """TODO: Description."""

    schema = _schema

    def __init__(self):
        super().__init__("recordings")

    # ----- create -----
    @operation(
        params = {
            "_body": _schema.properties["content"],
        },
        returns = s.dict({"id": _schema.properties["id"]}),
    )
    def create(self, id, _body):
        pass

    # ----- read -----
    @operation(
        params = {
            "id": _schema.properties["id"],
        },
        returns = _schema.properties["content"],
    )
    def read(self, id):
        pass
