from pyUbiForge2.api.game import SubclassBaseFile
from .CharacterBehaviorData import CharacterBehaviorData as _CharacterBehaviorData


class NPCBehaviorData(SubclassBaseFile):
    ResourceType = 0x81C08821
    ParentResourceType = _CharacterBehaviorData.ResourceType
    parent: _CharacterBehaviorData
