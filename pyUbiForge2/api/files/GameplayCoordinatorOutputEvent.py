from pyUbiForge2.api.game import SubclassBaseFile
from .Event import Event as _Event


class GameplayCoordinatorOutputEvent(SubclassBaseFile):
    ResourceType = 0x1CE64005
    ParentResourceType = _Event.ResourceType
    parent: _Event
