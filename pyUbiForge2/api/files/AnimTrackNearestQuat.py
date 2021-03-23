from pyUbiForge2.api.game import SubclassBaseFile
from .AnimTrackQuat import AnimTrackQuat as _AnimTrackQuat


class AnimTrackNearestQuat(SubclassBaseFile):
    ResourceType = 0xD343DE8B
    ParentResourceType = _AnimTrackQuat.ResourceType
    parent: _AnimTrackQuat

