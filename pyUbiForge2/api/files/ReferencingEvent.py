from pyUbiForge2.api.game import SubclassBaseFile
from .Event import Event as _Event


class ReferencingEvent(SubclassBaseFile):
    ResourceType = 0xCB9B3D2F
    ParentResourceType = _Event.ResourceType
    parent: _Event

