from pyUbiForge2.api.game import SubclassBaseFile
from .AnimTrackQuat import AnimTrackQuat as _AnimTrackQuat


class AnimTrackLinearQuat(SubclassBaseFile):
    ResourceType = 0x4EF27AD8
    ParentResourceType = _AnimTrackQuat.ResourceType
    parent: _AnimTrackQuat
