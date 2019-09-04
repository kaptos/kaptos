"""TODO: Description."""

import roax.db
import roax.postgresql
import roax.postgis
import roax.schema as s
import uuid

from kaptos.config import config


_defaults = {
    "minconn": 1,
    "maxconn": 10,
    "dbname": "kaptos",
    "host": None,
    "port": None,
    "user": None,
    "password": None,
    "sslmode": None,
    "sslrootcert": None,
    "sslcert": None,
    "sslkey": None,
}


def _kwargs():
    result = {}
    dbc = config.get("database") or {}
    for key in _defaults:
        value = dbc.get(key) or _defaults[key]
        if value is not None:
            result[key] = value
    return result


database = roax.postgresql.Database(**_kwargs())


adapters = {
    **roax.postgis.adapters,
    s.set: roax.db.Adapter(),
    s.list: roax.db.Adapter(),
}


class Table(roax.db.Table):
    """Represents a Kaptos database table."""

    def __init__(self, name, schema):
        """
        :param name: Name of database table.
        :param schema: Schema of table columns.
        """
        super().__init__(database, name, schema, "id", adapters)


class TableResource(roax.db.TableResource):
    """Base class for Kaptos database resources."""

    def __init__(self):
        """TODO: Description."""
        super().__init__(Table(self.name, self.schema))

    def create(self, _body):
        """
        Create resource item.
        
        :param _body: The resource item content.
        :return: {"id": created item identifier}
        """
        _body = {**_body, "id": uuid.uuid4()}
        return super().create(_body["id"], _body)
