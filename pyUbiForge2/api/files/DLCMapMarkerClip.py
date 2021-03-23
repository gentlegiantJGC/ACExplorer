from pyUbiForge2.api.game import SubclassBaseFile
from .Clip import Clip as _Clip


class DLCMapMarkerClip(SubclassBaseFile):
    ResourceType = 0xA3B3ACDC
    ParentResourceType = _Clip.ResourceType
    parent: _Clip

