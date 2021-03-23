from pyUbiForge2.api.game import SubclassBaseFile
from .AnimTrackVec import AnimTrackVec as _AnimTrackVec


class AnimTrackVec4(SubclassBaseFile):
    ResourceType = 0xE21AF9CD
    ParentResourceType = _AnimTrackVec.ResourceType
    parent: _AnimTrackVec
