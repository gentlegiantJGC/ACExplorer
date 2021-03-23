from pyUbiForge2.api.game import SubclassBaseFile
from .Event import Event as _Event


class FocusQueryEvent(SubclassBaseFile):
    ResourceType = 0x6F81EE79
    ParentResourceType = _Event.ResourceType
    parent: _Event

