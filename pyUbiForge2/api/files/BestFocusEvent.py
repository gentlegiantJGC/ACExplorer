from pyUbiForge2.api.game import SubclassBaseFile
from .Event import Event as _Event


class BestFocusEvent(SubclassBaseFile):
    ResourceType = 0xC5FFBF2F
    ParentResourceType = _Event.ResourceType
    parent: _Event
