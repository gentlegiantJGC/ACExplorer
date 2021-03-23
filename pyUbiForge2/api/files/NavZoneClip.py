from pyUbiForge2.api.game import SubclassBaseFile
from .Clip import Clip as _Clip


class NavZoneClip(SubclassBaseFile):
    ResourceType = 0xA4477744
    ParentResourceType = _Clip.ResourceType
    parent: _Clip

