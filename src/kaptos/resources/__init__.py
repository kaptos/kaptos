"""Kaptos resources module."""

from ..config import config
from collections import Mapping
from pymongo import MongoClient
from roax.mongodb import MongoResource
from roax.patch import merge_patch
from roax.resource import BadRequest, Resources
from uuid import uuid4

_client = MongoClient(config["mongo_host"], config.get("mongo_port"))
_db = _client["kaptos"]


class KaptosResource(Resource):
    """
    Base class for Kaptos resources. Performs optional caching of items.
    """

    def __init__(self, name, schema=None, cache_size=None, cache_ttl=None):
        """
        Initialize Kaptos resource.

        If one (or both) of `cache_size` or `cache_ttl` are specified, then items are
        cached by an underlying in-memory resource.

        :param name: Short name of the resource. [class name in lower case]
        :param schema: Schema for resource items; can be supplied as class or instance variable.
        :param cache_size: Maximum number of items to store. [unlimited]
        :param cache_ttl: Maximum item time to live, in seconds. [unlimited]
        """
        super().__init__(name)
        self.schema = schema or self.schema
        self.store = MongoResource(collection=_db[name], name=name, schema=self.schema)
        self.cache = None
        if cache_size or cache_ttl:
            self.cache = MemoryResource(size=cache_size, ttl=cache_ttl, evict=True)

    def create(self, _body)
        """
        Create resource item.
        
        :param _body: The resource item content.
        :returns: {"id": created resource item identifier}
        :raises NotFound: If resource item not found.
        """
        _body = {**_body, "id": uuid4()}
        return self.store.create(_body["id"], _body)

    def read(self, id):
        """
        Read resource item.
        
        :param id: Identifies resource item to read.
        :returns: The read resource item.
        :raises NotFound: If resource item not found.
        """
        if self.cache:
            try:
                return self.cache.read(id)
            except NotFound:
                pass
        result = self.store.read(id)
        result["id"] = id
        if self.cache:
            self.cache.create(id, result)
        return result

    def update(self, id, _body, mask=None):
        """
        Perform full modification of resource item.
        
        :param id: Identifies resource item to update.
        :param _body: Content to update resource item with.
        :raises NotFound: If resource item not found.
        """
        _body = {**_body, "id": id}
        self.store.update(id, _body)
        self.invalidate(id)

    def delete(self, id):
        """
        Delete resource item.
        
        :param id: Identifies resource item to delete.
        :raises NotFound: If resource item not found.
        """
        self.store.delete(id)
        self.invalidate(id)

    def patch(self, id, _body, mask=None):
        """
        Perform partial modification of resource item with merge-patch document.

        :param id: Identifies resource item to patch.
        :param _body: The merge-patch document to apply to resource item content.
        :param mask: Set of properties allowed to be modified.
        :raises NotFound: If resource item not found.
        """
        if not isinstance(_body, Mapping):
            raise BadRequest("patch document must be a key-value mapping")
        patch = {k: v for k, v in _body.items() if not mask or k in mask}
        self.update(id, merge_patch(self.read(id), patch))  # invalidates cache

    def invalidate(self, id):
        """
        Invalidate one or all cache entries.

        :param id: identifies entry to invalidate, or `None` for all entries.
        """
        if self.cache:
            if id:
                try:
                    self.cache.delete(id)
                except NotFound:
                    pass
            else:
                self.cache.clear()


resources = Resources({
    "members": "kaptos.resources.v1.members.Members",
    "organizations": "kaptos.resources.v1.organizations.Organizations",
    "recordings": "kaptos.resources.v1.recordings.Recordings",
    "reports": "kaptos.resources.v1.reports.Reports",
    "sessions": "kaptos.resources.v1.sessions.Sessions",
    "stations": "kaptos.resources.v1.stations.Stations",
    "tasks": "kaptos.resources.v1.tasks.Tasks",
    "transmissions": "kaptos.resources.v1.transmissions.Transmissions",
    "users": "kaptos.resources.v1.users.Users",
})
