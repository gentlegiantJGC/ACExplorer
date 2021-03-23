from pyUbiForge2.api.game import SubclassBaseFile
from .Event import Event as _Event


class DangerEvent(SubclassBaseFile):
    ResourceType = 0xAB86EE9A
    ParentResourceType = _Event.ResourceType
    parent: _Event

