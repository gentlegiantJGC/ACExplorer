from pyUbiForge2.api.game import SubclassBaseFile
from .AnimTrackByte import AnimTrackByte as _AnimTrackByte


class AnimTrackNearestByte(SubclassBaseFile):
    ResourceType = 0xC5F01978
    ParentResourceType = _AnimTrackByte.ResourceType
    parent: _AnimTrackByte
