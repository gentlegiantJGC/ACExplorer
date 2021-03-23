from pyUbiForge2.api.game import SubclassBaseFile
from .AnimTrackInt import AnimTrackInt as _AnimTrackInt


class AnimTrackLinearInt(SubclassBaseFile):
    ResourceType = 0x2F4D2109
    ParentResourceType = _AnimTrackInt.ResourceType
    parent: _AnimTrackInt
