from pyUbiForge2.api.game import SubclassBaseFile
from .Clip import Clip as _Clip


class JumpClip(SubclassBaseFile):
    ResourceType = 0x02C166CE
    ParentResourceType = _Clip.ResourceType
    parent: _Clip
