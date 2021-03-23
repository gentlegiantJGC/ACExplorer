from pyUbiForge2.api.game import SubclassBaseFile
from .AnimTrackValue import AnimTrackValue as _AnimTrackValue


class AnimTrackFloat(SubclassBaseFile):
    ResourceType = 0xB3637621
    ParentResourceType = _AnimTrackValue.ResourceType
    parent: _AnimTrackValue
