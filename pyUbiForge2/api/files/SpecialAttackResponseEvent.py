from pyUbiForge2.api.game import SubclassBaseFile
from .Event import Event as _Event


class SpecialAttackResponseEvent(SubclassBaseFile):
    ResourceType = 0x7F403534
    ParentResourceType = _Event.ResourceType
    parent: _Event

