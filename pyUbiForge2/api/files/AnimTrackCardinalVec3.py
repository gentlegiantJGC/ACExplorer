from pyUbiForge2.api.game import SubclassBaseFile
from .AnimTrackVec3 import AnimTrackVec3 as _AnimTrackVec3


class AnimTrackCardinalVec3(SubclassBaseFile):
    ResourceType = 0xC15FCF55
    ParentResourceType = _AnimTrackVec3.ResourceType
    parent: _AnimTrackVec3
