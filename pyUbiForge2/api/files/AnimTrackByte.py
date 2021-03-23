from pyUbiForge2.api.game import SubclassBaseFile
from .AnimTrackValue import AnimTrackValue as _AnimTrackValue


class AnimTrackByte(SubclassBaseFile):
    ResourceType = 0x31B286E5
    ParentResourceType = _AnimTrackValue.ResourceType
    parent: _AnimTrackValue
