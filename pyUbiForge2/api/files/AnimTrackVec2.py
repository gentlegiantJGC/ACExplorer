from pyUbiForge2.api.game import SubclassBaseFile
from .AnimTrackVec import AnimTrackVec as _AnimTrackVec


class AnimTrackVec2(SubclassBaseFile):
    ResourceType = 0x0B795CF8
    ParentResourceType = _AnimTrackVec.ResourceType
    parent: _AnimTrackVec

