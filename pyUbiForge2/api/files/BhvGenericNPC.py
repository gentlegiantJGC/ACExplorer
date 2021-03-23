from pyUbiForge2.api.game import SubclassBaseFile
from .CharacterBehavior import CharacterBehavior as _CharacterBehavior


class BhvGenericNPC(SubclassBaseFile):
    ResourceType = 0x3D02D8AC
    ParentResourceType = _CharacterBehavior.ResourceType
    parent: _CharacterBehavior

