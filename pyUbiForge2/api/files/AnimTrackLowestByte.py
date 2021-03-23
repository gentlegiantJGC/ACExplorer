from pyUbiForge2.api.game import SubclassBaseFile
from .AnimTrackByte import AnimTrackByte as _AnimTrackByte


class AnimTrackLowestByte(SubclassBaseFile):
    ResourceType = 0x89F1B891
    ParentResourceType = _AnimTrackByte.ResourceType
    parent: _AnimTrackByte

