from pyUbiForge2.api.game import SubclassBaseFile
from .Event import Event as _Event


class FightStrategyPositionNotOKEvent(SubclassBaseFile):
    ResourceType = 0x7E11370E
    ParentResourceType = _Event.ResourceType
    parent: _Event
