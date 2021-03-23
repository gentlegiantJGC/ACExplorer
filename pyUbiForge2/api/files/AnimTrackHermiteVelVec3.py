from pyUbiForge2.api.game import SubclassBaseFile
from .AnimTrackVec3 import AnimTrackVec3 as _AnimTrackVec3


class AnimTrackHermiteVelVec3(SubclassBaseFile):
    ResourceType = 0x198FE2F6
    ParentResourceType = _AnimTrackVec3.ResourceType
    parent: _AnimTrackVec3

