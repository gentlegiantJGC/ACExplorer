from pyUbiForge2.api.game import SubclassBaseFile
from .Clip import Clip as _Clip


class CrowdDensityClip(SubclassBaseFile):
    ResourceType = 0xC265BD12
    ParentResourceType = _Clip.ResourceType
    parent: _Clip
