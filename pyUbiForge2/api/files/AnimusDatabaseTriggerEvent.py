from pyUbiForge2.api.game import SubclassBaseFile
from .Event import Event as _Event


class AnimusDatabaseTriggerEvent(SubclassBaseFile):
    ResourceType = 0xE0D55B98
    ParentResourceType = _Event.ResourceType
    parent: _Event
