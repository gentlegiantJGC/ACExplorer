from pyUbiForge2.api.game import SubclassBaseFile
from .Clip import Clip as _Clip


class HorseMountingClip(SubclassBaseFile):
    ResourceType = 0x04B552E0
    ParentResourceType = _Clip.ResourceType
    parent: _Clip
