from pyUbiForge2.api.game import SubclassBaseFile
from .Event import Event as _Event


class BloodSplatterEvent(SubclassBaseFile):
    ResourceType = 0xD84E267F
    ParentResourceType = _Event.ResourceType
    parent: _Event
