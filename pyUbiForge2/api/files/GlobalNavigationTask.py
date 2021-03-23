from pyUbiForge2.api.game import SubclassBaseFile
from .CharacterTask import CharacterTask as _CharacterTask


class GlobalNavigationTask(SubclassBaseFile):
    ResourceType = 0x8DB5A2A6
    ParentResourceType = _CharacterTask.ResourceType
    parent: _CharacterTask
