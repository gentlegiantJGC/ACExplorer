from pyUbiForge2.api.game import SubclassBaseFile
from .AnimTrackInt import AnimTrackInt as _AnimTrackInt


class AnimTrackNearestInt(SubclassBaseFile):
    ResourceType = 0x4C9EDD8C
    ParentResourceType = _AnimTrackInt.ResourceType
    parent: _AnimTrackInt

