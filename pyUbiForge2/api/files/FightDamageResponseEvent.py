from pyUbiForge2.api.game import SubclassBaseFile
from .Event import Event as _Event


class FightDamageResponseEvent(SubclassBaseFile):
    ResourceType = 0x9459F3E0
    ParentResourceType = _Event.ResourceType
    parent: _Event
