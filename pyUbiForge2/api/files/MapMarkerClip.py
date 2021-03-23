from pyUbiForge2.api.game import SubclassBaseFile
from .Clip import Clip as _Clip


class MapMarkerClip(SubclassBaseFile):
    ResourceType = 0x08E51BC5
    ParentResourceType = _Clip.ResourceType
    parent: _Clip

