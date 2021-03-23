from pyUbiForge2.api.game import SubclassBaseFile
from .AnimTrackVec3 import AnimTrackVec3 as _AnimTrackVec3


class AnimTrackLinearVec3(SubclassBaseFile):
    ResourceType = 0x158D57A0
    ParentResourceType = _AnimTrackVec3.ResourceType
    parent: _AnimTrackVec3

