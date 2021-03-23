from pyUbiForge2.api.game import SubclassBaseFile
from .AnimTrackQuat16 import AnimTrackQuat16 as _AnimTrackQuat16


class AnimTrackLinearQuat16(SubclassBaseFile):
    ResourceType = 0xB10F1913
    ParentResourceType = _AnimTrackQuat16.ResourceType
    parent: _AnimTrackQuat16
