"""Tokens for accessing Kaptos server."""

import dataclasses
import kaptos.db
import roax.schema as s

from roax.resource import operation


@dataclasses.dataclass
class Token:
    """Token for accessing Kaptos server."""

    id: s.uuid(description="Identifies the token.")
    type: s.str(description="Token type.", enum={"password", "session", "reset"})
    value: s.str(description="Token value.")
    subject: s.uuid(description="Reference to subject of token.")
    created: s.datetime(description="Date and time token was created.")
    expires: s.datetime(description="Date and time token expires.")

    _required = "type value subject created"


schema = s.dataclass(Token)


class Tokens(kaptos.db.TableResource):

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
