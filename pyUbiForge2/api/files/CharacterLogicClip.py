from pyUbiForge2.api.game import SubclassBaseFile
from .MultiEntitiesClip import MultiEntitiesClip as _MultiEntitiesClip


class CharacterLogicClip(SubclassBaseFile):
    ResourceType = 0x6FCD074A
    ParentResourceType = _MultiEntitiesClip.ResourceType
    parent: _MultiEntitiesClip
