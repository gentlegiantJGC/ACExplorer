from pyUbiForge2.api.game import SubclassBaseFile
from .AIComponent import AIComponent as _AIComponent


class CharacterBehavior(SubclassBaseFile):
    ResourceType = 0xF193915C
    ParentResourceType = _AIComponent.ResourceType
    parent: _AIComponent
