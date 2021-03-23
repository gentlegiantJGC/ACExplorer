from pyUbiForge2.api.game import SubclassBaseFile
from .Clip import Clip as _Clip


class AnimusDatabaseClip(SubclassBaseFile):
    ResourceType = 0x6A45A972
    ParentResourceType = _Clip.ResourceType
    parent: _Clip
