from pyUbiForge2.api.game import SubclassBaseFile
from .Event import Event as _Event


class GliderGameplayEvent(SubclassBaseFile):
    ResourceType = 0x36569D5D
    ParentResourceType = _Event.ResourceType
    parent: _Event
