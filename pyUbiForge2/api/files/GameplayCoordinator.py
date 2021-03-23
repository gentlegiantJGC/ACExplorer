from pyUbiForge2.api.game import SubclassBaseFile
from .AbstractGameplayCoordinator import (
    AbstractGameplayCoordinator as _AbstractGameplayCoordinator,
)


class GameplayCoordinator(SubclassBaseFile):
    ResourceType = 0xC5F33877
    ParentResourceType = _AbstractGameplayCoordinator.ResourceType
    parent: _AbstractGameplayCoordinator
