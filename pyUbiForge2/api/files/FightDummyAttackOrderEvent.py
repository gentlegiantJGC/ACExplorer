from pyUbiForge2.api.game import SubclassBaseFile
from .Event import Event as _Event


class FightDummyAttackOrderEvent(SubclassBaseFile):
    ResourceType = 0x86381698
    ParentResourceType = _Event.ResourceType
    parent: _Event

