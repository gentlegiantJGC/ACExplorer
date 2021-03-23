from pyUbiForge2.api.game import SubclassBaseFile
from .Event import Event as _Event


class GameplayCoordinatorEvent(SubclassBaseFile):
    ResourceType = 0x850D27B0
    ParentResourceType = _Event.ResourceType
    parent: _Event
