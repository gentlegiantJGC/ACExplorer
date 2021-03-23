from pyUbiForge2.api.game import SubclassBaseFile
from .Clip import Clip as _Clip


class SpecialCounterClip(SubclassBaseFile):
    ResourceType = 0x4EA3742F
    ParentResourceType = _Clip.ResourceType
    parent: _Clip
