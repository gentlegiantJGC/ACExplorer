from pyUbiForge2.api.game import SubclassBaseFile
from .AnimTrackByte import AnimTrackByte as _AnimTrackByte


class AnimTrackLinearByte(SubclassBaseFile):
    ResourceType = 0x5841BD2B
    ParentResourceType = _AnimTrackByte.ResourceType
    parent: _AnimTrackByte
