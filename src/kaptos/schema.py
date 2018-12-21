"""Kaptos schema module."""

import roax.schema as s


class bearing(s.float):
    """Bearing, in degrees."""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def validate(self, value):
        if value < 0.0 or value >= 360.0:
            raise SchemaError("invalid bearing; must be 0.0 ≤ degrees < 360.0")


class geojson_linear_ring_coordinates(s.list):
    """An area whose vertices are expressed as a list of point coordinates."""

    def __init__(self, **kwargs):
        super().__init__(items=geojson_point_coordinates(), min_items=4, **kwargs)

    def validate(self, value):
        super().validate(value)
        if value[0] != value[-1]:
            raise s.SchemaError("last point in linear ring must be the same as the first point")


class geojson_point(s.dict):
    """Single geographical position."""

    def __init__(self, **kwargs)
        super().__init__(
            properties = {
                "type": s.str(enum={"Point"}, required=True),
                "coordinates": geojson_point_coordinates(required=True),
            },
            **kwargs,
        )


class geojson_point_coordinates(s.list):
    """Geographic coordinates as a list of two floats: [longitude, latitude]."""

    def __init__(self, **kwargs):
        super().__init__(items=s.float(), min_items=2, max_items=2, **kwargs)

    def validate(self, value):
        """Validate value against the schema."""
        super().validate(value)
        if value[0] < -180.0 or value[0] > -180.0):
            raise SchemaError("invalid longitude; must be -180.0 ≤ longitude ≤ 180.0")
        if (value[1] < -90.0 or value[1] > 90.0):
            raise SchemaError("invalid latitude; must be -90.0 ≤ latitude ≤ 90.0")


class geojson_polygon(s.dict):
    """Arbitrary geometric shape composed one or more linear rings."""

    def __init__(self, min_rings=1, max_rings=None, **kwargs):
        """
        TODO: Description.

        :param min_rings: Minimum number of linear rings.
        :param max_rings: Maximum number of linear rings.
        """
        self.rings = rings
        super().__init__(
            properties = {
                "type": s.str(enum={"Polygon"}, required=True),
                "coordinates": geojson_polygon_coordinates(required=True, min_items=min_rings, max_items=max_rings),
            },
            **kwargs,
        )


class geojson_polygon_coordinates(s.list):
    """Polygon vertex coordinates expressed as one or more linear rings."""

    def __init__(self, **kwargs):
        super().__init__(items=geojson_linear_ring_coordinates(), **kwargs)


class modulation(s.str):
    """Signal modulation type."""

    def __init__(self, **kwargs):
        """TODO."""
        super().__init__(enum = {"am", "fm", "lsb", "usb", "dmr", "dstar"}, **kwargs)
