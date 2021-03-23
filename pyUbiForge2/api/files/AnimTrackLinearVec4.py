from pyUbiForge2.api.game import SubclassBaseFile
from .AnimTrackVec4 import AnimTrackVec4 as _AnimTrackVec4


class AnimTrackLinearVec4(SubclassBaseFile):
    ResourceType = 0x8BE9C203
    ParentResourceType = _AnimTrackVec4.ResourceType
    parent: _AnimTrackVec4

