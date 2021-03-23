from pyUbiForge2.api.game import SubclassBaseFile
from .GameplayCoordinatorManager import (
    GameplayCoordinatorManager as _GameplayCoordinatorManager,
)


class DefaultGameplayCoordinatorManager(SubclassBaseFile):
    ResourceType = 0x22E11589
    ParentResourceType = _GameplayCoordinatorManager.ResourceType
    parent: _GameplayCoordinatorManager
