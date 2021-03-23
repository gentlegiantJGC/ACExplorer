from pyUbiForge2.api.game import SubclassBaseFile
from .CharacterBehaviorData import CharacterBehaviorData as _CharacterBehaviorData


class BhvAssassinData(SubclassBaseFile):
    ResourceType = 0xDB7B4621
    ParentResourceType = _CharacterBehaviorData.ResourceType
    parent: _CharacterBehaviorData
