from pyUbiForge2.api.game import SubclassBaseFile
from .CharacterBehavior import CharacterBehavior as _CharacterBehavior


class BhvHorse(SubclassBaseFile):
    ResourceType = 0x7F31B837
    ParentResourceType = _CharacterBehavior.ResourceType
    parent: _CharacterBehavior

