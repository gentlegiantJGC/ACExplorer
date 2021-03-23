from pyUbiForge2.api.game import SubclassBaseFile
from .Clip import Clip as _Clip


class GroupBubbleClip(SubclassBaseFile):
    ResourceType = 0x4A4E5340
    ParentResourceType = _Clip.ResourceType
    parent: _Clip

