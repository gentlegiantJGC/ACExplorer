from pyUbiForge2.api.game import SubclassBaseFile
from .Event import Event as _Event


class MenuChoiceMadeEvent(SubclassBaseFile):
    ResourceType = 0x1A775B68
    ParentResourceType = _Event.ResourceType
    parent: _Event
