from pyUbiForge2.api.game import SubclassBaseFile
from .InGameMenuEvent import InGameMenuEvent as _InGameMenuEvent


class AllowInGameMenuEvent(SubclassBaseFile):
    ResourceType = 0x977032B4
    ParentResourceType = _InGameMenuEvent.ResourceType
    parent: _InGameMenuEvent
