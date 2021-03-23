from pyUbiForge2.api.game import SubclassBaseFile
from .GameplayEvent import GameplayEvent as _GameplayEvent


class GameplayHighToleranceEvent(SubclassBaseFile):
    ResourceType = 0x7F23DA38
    ParentResourceType = _GameplayEvent.ResourceType
    parent: _GameplayEvent
