from pyUbiForge2.api.game import SubclassBaseFile
from .Clip import Clip as _Clip


class AnimSetClip(SubclassBaseFile):
    ResourceType = 0x62418E1C
    ParentResourceType = _Clip.ResourceType
    parent: _Clip
