from pyUbiForge2.api.game import SubclassBaseFile
from .AITask import AITask as _AITask


class CharacterTask(SubclassBaseFile):
    ResourceType = 0x47F3FD8A
    ParentResourceType = _AITask.ResourceType
    parent: _AITask
