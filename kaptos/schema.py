"""Kaptos schema module."""

import roax.schema as s


class bearing(s.float):
    """Bearing, in degrees."""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def validate(self, value):
        if value < 0.0 or value >= 360.0:
            raise SchemaError("invalid bearing; must be 0.0 ≤ degrees < 360.0")


class modulation(s.str):
    """Signal modulation type."""

    def __init__(self, **kwargs):
        super().__init__(enum={"am", "fm", "lsb", "usb", "dmr", "dstar"})
