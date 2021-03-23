from pyUbiForge2.api.game import SubclassBaseFile
from .CharacterBehavior import CharacterBehavior as _CharacterBehavior


class NPCBehavior(SubclassBaseFile):
    ResourceType = 0x164D2700
    ParentResourceType = _CharacterBehavior.ResourceType
    parent: _CharacterBehavior
