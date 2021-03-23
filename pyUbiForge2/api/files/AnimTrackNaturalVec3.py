from pyUbiForge2.api.game import SubclassBaseFile
from .AnimTrackVec3 import AnimTrackVec3 as _AnimTrackVec3


class AnimTrackNaturalVec3(SubclassBaseFile):
    ResourceType = 0xD1B2803D
    ParentResourceType = _AnimTrackVec3.ResourceType
    parent: _AnimTrackVec3

