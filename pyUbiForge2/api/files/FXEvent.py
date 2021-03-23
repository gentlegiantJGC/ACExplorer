from pyUbiForge2.api.game import SubclassBaseFile
from .Event import Event as _Event


class FXEvent(SubclassBaseFile):
    ResourceType = 0x6627C719
    ParentResourceType = _Event.ResourceType
    parent: _Event
