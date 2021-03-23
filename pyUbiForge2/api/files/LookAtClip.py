from pyUbiForge2.api.game import SubclassBaseFile
from .Clip import Clip as _Clip


class LookAtClip(SubclassBaseFile):
    ResourceType = 0x80AC90A6
    ParentResourceType = _Clip.ResourceType
    parent: _Clip

