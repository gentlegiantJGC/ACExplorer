from pyUbiForge2.api.game import SubclassBaseFile
from .Clip import Clip as _Clip


class RopeCutClip(SubclassBaseFile):
    ResourceType = 0x0D193622
    ParentResourceType = _Clip.ResourceType
    parent: _Clip
