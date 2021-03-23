from pyUbiForge2.api.game import SubclassBaseFile
from .CharacterTask import CharacterTask as _CharacterTask


class AssassinTask(SubclassBaseFile):
    ResourceType = 0xC41BC202
    ParentResourceType = _CharacterTask.ResourceType
    parent: _CharacterTask

