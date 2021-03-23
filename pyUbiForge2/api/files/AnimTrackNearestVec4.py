from pyUbiForge2.api.game import SubclassBaseFile
from .AnimTrackVec4 import AnimTrackVec4 as _AnimTrackVec4


class AnimTrackNearestVec4(SubclassBaseFile):
    ResourceType = 0x16586650
    ParentResourceType = _AnimTrackVec4.ResourceType
    parent: _AnimTrackVec4
