from pyUbiForge2.api.game import SubclassBaseFile
from .AnimTrackQuat64 import AnimTrackQuat64 as _AnimTrackQuat64


class AnimTrackLinearQuat64(SubclassBaseFile):
    ResourceType = 0x1040EEF8
    ParentResourceType = _AnimTrackQuat64.ResourceType
    parent: _AnimTrackQuat64
