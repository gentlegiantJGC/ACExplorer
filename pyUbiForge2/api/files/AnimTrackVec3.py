from pyUbiForge2.api.game import SubclassBaseFile
from .AnimTrackVec import AnimTrackVec as _AnimTrackVec


class AnimTrackVec3(SubclassBaseFile):
    ResourceType = 0x7C7E6C6E
    ParentResourceType = _AnimTrackVec.ResourceType
    parent: _AnimTrackVec
