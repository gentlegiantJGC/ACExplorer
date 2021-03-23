from pyUbiForge2.api.game import SubclassBaseFile
from .Event import Event as _Event


class MissionGameplayTimeBonusEvent(SubclassBaseFile):
    ResourceType = 0xA7AF44B2
    ParentResourceType = _Event.ResourceType
    parent: _Event

