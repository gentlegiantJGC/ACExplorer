from pyUbiForge2.api.game import SubclassBaseFile
from .AnimTrackVec2 import AnimTrackVec2 as _AnimTrackVec2


class AnimTrackLinearVec2(SubclassBaseFile):
    ResourceType = 0x628A6736
    ParentResourceType = _AnimTrackVec2.ResourceType
    parent: _AnimTrackVec2

