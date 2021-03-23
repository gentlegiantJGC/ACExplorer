from pyUbiForge2.api.game import SubclassBaseFile
from .GameplayCoordinatorEvent import (
    GameplayCoordinatorEvent as _GameplayCoordinatorEvent,
)


class GameplayCoordinatorAbortEvent(SubclassBaseFile):
    ResourceType = 0x50181C18
    ParentResourceType = _GameplayCoordinatorEvent.ResourceType
    parent: _GameplayCoordinatorEvent
