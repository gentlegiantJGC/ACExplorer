from pyUbiForge2.api.game import SubclassBaseFile
from .CharacterBehavior import CharacterBehavior as _CharacterBehavior


class BhvAssassin(SubclassBaseFile):
    ResourceType = 0xDB3596AB
    ParentResourceType = _CharacterBehavior.ResourceType
    parent: _CharacterBehavior

