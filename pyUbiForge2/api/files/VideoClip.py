from pyUbiForge2.api.game import SubclassBaseFile
from .Clip import Clip as _Clip


class VideoClip(SubclassBaseFile):
    ResourceType = 0x3811E504
    ParentResourceType = _Clip.ResourceType
    parent: _Clip
