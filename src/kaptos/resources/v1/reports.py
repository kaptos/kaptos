"""Station reception reports."""

import kaptos.schema as ks
import roax.schema as

from .. import KaptosResource
from roax.resource import operation


_schema = s.dict(
    description = "Station reception report.",
    properties = {
        "id": s.uuid(
            description = "Identifies the reception report.",
        ),
        "task_id": s.uuid(
            description = "Identifies the task that reception report is for.",
        ),
        "station_id": s.uuid(            
            description = "Identifies the station filing the reception report.",
        ),
        "time": s.datetime(
            description = "Date and time that the signal was received.",
        ),
        "frequency": s.int(
            description = "Frequency of received signal, in hertz.",
        ),
        "modulation": ks.modulation(
            description = "Modulation of received signal.",
        ),
        "location": ks.geojson_point(
            description = "Location of the receiving station at the time of reception.",
        ),
        "bearing": ks.bearing(
            description = "Bearing toward received signal, in degrees true.",
        ),
        "duration": s.int(
            description = "Duration of received signal, in seconds rounded-up.",
            min_value = 1,
        ),
        "strength": s.int(
            description = "Strength of the received signal, in dBm.",
        ),
        "nmea": s.str(
            description = "$GPRMC NMEA sentence received from GPS at the time the signal was detected.",
        ),
        "recording_id": s.uuid(
            description = "Identifies the recording of reported signal.",
        )
    },
    required = "task_id,station_id,time,frequency,modulation,location,bearing,duration,strength,nmea",
)

class Reports(KaptosResource):
    """TODO: Description."""

    schema = _schema

    def __init__(self):
        super().__init__("reports")

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
