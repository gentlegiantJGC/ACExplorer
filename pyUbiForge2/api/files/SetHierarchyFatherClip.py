from pyUbiForge2.api.game import SubclassBaseFile
from .Clip import Clip as _Clip


class SetHierarchyFatherClip(SubclassBaseFile):
    ResourceType = 0x4E6F39BB
    ParentResourceType = _Clip.ResourceType
    parent: _Clip

