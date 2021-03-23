from pyUbiForge2.api.game import SubclassBaseFile
from .Event import Event as _Event


class GameStatsEvent(SubclassBaseFile):
    ResourceType = 0xFB2526EF
    ParentResourceType = _Event.ResourceType
    parent: _Event

