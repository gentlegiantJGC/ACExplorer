from pyUbiForge2.api.game import SubclassBaseFile
from .AnimTrackQuat48 import AnimTrackQuat48 as _AnimTrackQuat48


class AnimTrackLinearQuat48(SubclassBaseFile):
    ResourceType = 0x2BC0C051
    ParentResourceType = _AnimTrackQuat48.ResourceType
    parent: _AnimTrackQuat48
