from pyUbiForge2.api.game import SubclassBaseFile
from .Event import Event as _Event


class FightManagerEnemiesOverFlowEvent(SubclassBaseFile):
    ResourceType = 0x4DDEA9BB
    ParentResourceType = _Event.ResourceType
    parent: _Event
