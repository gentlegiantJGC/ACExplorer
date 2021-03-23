from pyUbiForge2.api.game import SubclassBaseFile
from .Event import Event as _Event


class MissionGameplayLocateTargetEvent(SubclassBaseFile):
    ResourceType = 0xD8450D1F
    ParentResourceType = _Event.ResourceType
    parent: _Event
