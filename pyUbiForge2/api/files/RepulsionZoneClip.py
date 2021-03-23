from pyUbiForge2.api.game import SubclassBaseFile
from .Clip import Clip as _Clip


class RepulsionZoneClip(SubclassBaseFile):
    ResourceType = 0xD2677661
    ParentResourceType = _Clip.ResourceType
    parent: _Clip
