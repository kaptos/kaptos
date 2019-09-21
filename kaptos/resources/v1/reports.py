"""Station reception reports."""

import dataclasses
import kaptos.db
import kaptos.schema as ks
import roax.geo
import roax.schema as s

from roax.resource import operation


@dataclasses.dataclass
class Report:
    """Station reception report."""

    id: s.uuid(description="Identifies the reception report.")
    task_id: s.uuid(description="Identifies the task that reception report is for.")
    station_id: s.uuid(
        description="Identifies the station filing the reception report."
    )
    time: s.datetime(description="Date and time that the signal was received.")
    frequency: s.int(description="Frequency of received signal, in hertz.")
    modulation: ks.modulation(description="Modulation of received signal.")
    location: roax.geo.Point(
        description="Location of the receiving station at the time of reception."
    )
    bearing: ks.bearing(description="Bearing toward received signal, in degrees true.")
    duration: s.int(
        description="Duration of received signal, in seconds rounded-up.", min=1
    )
    strength: s.int(description="Strength of the received signal, in dBm.")
    nmea: s.str(
        description="$GPRMC NMEA sentence received from GPS at the time the signal was detected."
    )

    _required = (
        "task_id station_id time frequency modulation location bearing duration strength nmea",
    )


schema = s.dataclass(Report)


class Reports(kaptos.db.TableResource):

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
