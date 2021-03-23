from pyUbiForge2.api.game import SubclassBaseFile
from .Clip import Clip as _Clip


class FXClip(SubclassBaseFile):
    ResourceType = 0x4CF6A89D
    ParentResourceType = _Clip.ResourceType
    parent: _Clip
