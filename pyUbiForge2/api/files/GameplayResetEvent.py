from pyUbiForge2.api.game import SubclassBaseFile
from .GameplayEvent import GameplayEvent as _GameplayEvent


class GameplayResetEvent(SubclassBaseFile):
    ResourceType = 0x3D4D7B85
    ParentResourceType = _GameplayEvent.ResourceType
    parent: _GameplayEvent
