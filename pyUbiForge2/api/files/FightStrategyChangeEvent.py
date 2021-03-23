from pyUbiForge2.api.game import SubclassBaseFile
from .Event import Event as _Event


class FightStrategyChangeEvent(SubclassBaseFile):
    ResourceType = 0x74508F1E
    ParentResourceType = _Event.ResourceType
    parent: _Event
