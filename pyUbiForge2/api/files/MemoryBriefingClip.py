from pyUbiForge2.api.game import SubclassBaseFile
from .Clip import Clip as _Clip


class MemoryBriefingClip(SubclassBaseFile):
    ResourceType = 0xC5ABAB54
    ParentResourceType = _Clip.ResourceType
    parent: _Clip

