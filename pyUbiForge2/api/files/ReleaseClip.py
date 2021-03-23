from pyUbiForge2.api.game import SubclassBaseFile
from .Clip import Clip as _Clip


class ReleaseClip(SubclassBaseFile):
    ResourceType = 0x83346214
    ParentResourceType = _Clip.ResourceType
    parent: _Clip
