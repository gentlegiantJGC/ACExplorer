from pyUbiForge2.api.game import SubclassBaseFile
from .Event import Event as _Event


class GrabEvent(SubclassBaseFile):
    ResourceType = 0x1CB75977
    ParentResourceType = _Event.ResourceType
    parent: _Event
