"""Station reception reports."""

import kaptos.db
import kaptos.schema as ks
import roax.geo
import roax.schema as s

from roax.resource import operation


schema = s.dict(
    description="Station reception report.",
    properties={
        "id": s.uuid(description="Identifies the reception report."),
        "task_id": s.uuid(
            description="Identifies the task that reception report is for."
        ),
        "station_id": s.uuid(
            description="Identifies the station filing the reception report."
        ),
        "time": s.datetime(description="Date and time that the signal was received."),
        "frequency": s.int(description="Frequency of received signal, in hertz."),
        "modulation": ks.modulation(description="Modulation of received signal."),
        "location": roax.geo.Point(
            description="Location of the receiving station at the time of reception."
        ),
        "bearing": ks.bearing(
            description="Bearing toward received signal, in degrees true."
        ),
        "duration": s.int(
            description="Duration of received signal, in seconds rounded-up.", minimum=1
        ),
        "strength": s.int(description="Strength of the received signal, in dBm."),
        "nmea": s.str(
            description="$GPRMC NMEA sentence received from GPS at the time the signal was detected."
        ),
        "recording_id": s.uuid(
            description="Identifies the recording of reported signal."
        ),
    },
    required={
        "task_id",
        "station_id",
        "time",
        "frequency",
        "modulation",
        "location",
        "bearing",
        "duration",
        "strength",
        "nmea",
    },
)


class Reports(kaptos.db.TableResource):

    name = "reports"

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
