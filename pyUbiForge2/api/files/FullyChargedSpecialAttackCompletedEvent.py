from pyUbiForge2.api.game import SubclassBaseFile
from .Event import Event as _Event


class FullyChargedSpecialAttackCompletedEvent(SubclassBaseFile):
    ResourceType = 0x804C6853
    ParentResourceType = _Event.ResourceType
    parent: _Event

