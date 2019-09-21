"""Teams of users and monitoring tasks within a geographic region."""

import dataclasses
import kaptos.db
import roax.geo
import roax.schema as s

from roax.resource import operation


@dataclasses.dataclass
class Team:
    """Team of users and monitoring tasks within a geographic region."""

    id: s.uuid(description="Identifies the team.")
    name: s.str(description="Name of the team.")
    description: s.str(description="Description of the team.")
    area: roax.geo.Polygon(
        description="Area from which signal reports will be accepted.", max_rings=1
    )
    visibility: s.str(
        description="Organization visibility.", enum={"public", "private"}
    )

    _required = "name description area visibility"


schema = s.dataclass(Team)


class Teams(kaptos.db.TableResource):

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
