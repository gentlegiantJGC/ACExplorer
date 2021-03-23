from pyUbiForge2.api.game import SubclassBaseFile
from .Clip import Clip as _Clip


class GlobalMapMarkerClip(SubclassBaseFile):
    ResourceType = 0x77F60E21
    ParentResourceType = _Clip.ResourceType
    parent: _Clip

