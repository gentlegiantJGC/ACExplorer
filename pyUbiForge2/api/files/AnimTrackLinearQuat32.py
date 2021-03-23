from pyUbiForge2.api.game import SubclassBaseFile
from .AnimTrackQuat32 import AnimTrackQuat32 as _AnimTrackQuat32


class AnimTrackLinearQuat32(SubclassBaseFile):
    ResourceType = 0x8454BF88
    ParentResourceType = _AnimTrackQuat32.ResourceType
    parent: _AnimTrackQuat32
