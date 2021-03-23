from pyUbiForge2.api.game import SubclassBaseFile
from .AnimTrackVec2 import AnimTrackVec2 as _AnimTrackVec2


class AnimTrackCardinalVec2(SubclassBaseFile):
    ResourceType = 0xB658FFC3
    ParentResourceType = _AnimTrackVec2.ResourceType
    parent: _AnimTrackVec2

