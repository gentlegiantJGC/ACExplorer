from pyUbiForge2.api.game import SubclassBaseFile
from .Event import Event as _Event


class StateChangeEvent(SubclassBaseFile):
    ResourceType = 0x73E2C961
    ParentResourceType = _Event.ResourceType
    parent: _Event

