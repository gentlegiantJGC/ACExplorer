from pyUbiForge2.api.game import SubclassBaseFile
from .Clip import Clip as _Clip


class AcquireClip(SubclassBaseFile):
    ResourceType = 0x60B9B956
    ParentResourceType = _Clip.ResourceType
    parent: _Clip
