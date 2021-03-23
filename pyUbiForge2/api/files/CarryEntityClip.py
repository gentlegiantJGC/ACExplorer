from pyUbiForge2.api.game import SubclassBaseFile
from .Clip import Clip as _Clip


class CarryEntityClip(SubclassBaseFile):
    ResourceType = 0x18106FCC
    ParentResourceType = _Clip.ResourceType
    parent: _Clip
