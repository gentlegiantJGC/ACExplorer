from pyUbiForge2.api.game import SubclassBaseFile
from .Event import Event as _Event


class FightStrategyPositionOKEvent(SubclassBaseFile):
    ResourceType = 0x882FAA96
    ParentResourceType = _Event.ResourceType
    parent: _Event
