from pyUbiForge2.api.game import SubclassBaseFile
from .Clip import Clip as _Clip


class MultiEntitiesClip(SubclassBaseFile):
    ResourceType = 0x076FC097
    ParentResourceType = _Clip.ResourceType
    parent: _Clip

