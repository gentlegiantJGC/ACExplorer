from pyUbiForge2.api.game import SubclassBaseFile
from .Event import Event as _Event


class NotorietyMissionActivationEvent(SubclassBaseFile):
    ResourceType = 0x9E7EBDE3
    ParentResourceType = _Event.ResourceType
    parent: _Event
