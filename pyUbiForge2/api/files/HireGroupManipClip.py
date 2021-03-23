from pyUbiForge2.api.game import SubclassBaseFile
from .Clip import Clip as _Clip


class HireGroupManipClip(SubclassBaseFile):
    ResourceType = 0x3EA71A9B
    ParentResourceType = _Clip.ResourceType
    parent: _Clip
