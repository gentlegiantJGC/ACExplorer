from pyUbiForge2.api.game import SubclassBaseFile
from .MultiEntitiesClip import MultiEntitiesClip as _MultiEntitiesClip


class KillClip(SubclassBaseFile):
    ResourceType = 0x005939CC
    ParentResourceType = _MultiEntitiesClip.ResourceType
    parent: _MultiEntitiesClip
