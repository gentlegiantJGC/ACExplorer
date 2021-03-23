from pyUbiForge2.api.game import SubclassBaseFile
from .Clip import Clip as _Clip


class AFSClip(SubclassBaseFile):
    ResourceType = 0xF5F4999C
    ParentResourceType = _Clip.ResourceType
    parent: _Clip
