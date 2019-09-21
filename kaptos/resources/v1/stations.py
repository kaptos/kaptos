"""Monitoring stations."""

import dataclasses
import kaptos.db
import roax.schema as s

from roax.resource import operation


@dataclasses.dataclass
class Station:
    """Monitoring station."""

    id: s.uuid(description="Identifies the station.")
    name: s.str(description="Station name.")
    description: s.str(description="Description of the station.")
    owner_id: s.uuid(description="Identifies the user who controls the station.")

    _required = "name description owner_id"


schema = s.dataclass(Station)


class Stations(kaptos.db.TableResource):

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
