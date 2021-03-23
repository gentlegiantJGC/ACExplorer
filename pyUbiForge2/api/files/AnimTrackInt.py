from pyUbiForge2.api.game import SubclassBaseFile
from .AnimTrackValue import AnimTrackValue as _AnimTrackValue


class AnimTrackInt(SubclassBaseFile):
    ResourceType = 0xDAB4119A
    ParentResourceType = _AnimTrackValue.ResourceType
    parent: _AnimTrackValue

