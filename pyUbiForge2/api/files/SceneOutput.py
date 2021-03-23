from pyUbiForge2.api.game import SubclassBaseFile
from .GameplayOutput import GameplayOutput as _GameplayOutput


class SceneOutput(SubclassBaseFile):
    ResourceType = 0xC0A01091
    ParentResourceType = _GameplayOutput.ResourceType
    parent: _GameplayOutput

