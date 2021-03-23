from pyUbiForge2.api.game import SubclassBaseFile
from .CharacterTask import CharacterTask as _CharacterTask


class FightTask(SubclassBaseFile):
    ResourceType = 0xF1C9C7E7
    ParentResourceType = _CharacterTask.ResourceType
    parent: _CharacterTask

