from pyUbiForge2.api.game import SubclassBaseFile
from .GameplayOutput import GameplayOutput as _GameplayOutput


class GameplayCoordinatorOutput(SubclassBaseFile):
    ResourceType = 0x4FB33274
    ParentResourceType = _GameplayOutput.ResourceType
    parent: _GameplayOutput

