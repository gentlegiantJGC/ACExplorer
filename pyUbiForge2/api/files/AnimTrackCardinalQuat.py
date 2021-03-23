from pyUbiForge2.api.game import SubclassBaseFile
from .AnimTrackLinearQuat import AnimTrackLinearQuat as _AnimTrackLinearQuat


class AnimTrackCardinalQuat(SubclassBaseFile):
    ResourceType = 0x9A20E22D
    ParentResourceType = _AnimTrackLinearQuat.ResourceType
    parent: _AnimTrackLinearQuat
