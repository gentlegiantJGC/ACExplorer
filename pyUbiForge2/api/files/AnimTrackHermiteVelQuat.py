from pyUbiForge2.api.game import SubclassBaseFile
from .AnimTrackQuat import AnimTrackQuat as _AnimTrackQuat


class AnimTrackHermiteVelQuat(SubclassBaseFile):
    ResourceType = 0x42F0CF8E
    ParentResourceType = _AnimTrackQuat.ResourceType
    parent: _AnimTrackQuat
