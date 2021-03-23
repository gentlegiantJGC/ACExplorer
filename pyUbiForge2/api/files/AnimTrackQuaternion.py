from pyUbiForge2.api.game import SubclassBaseFile
from .AnimTrackValue import AnimTrackValue as _AnimTrackValue


class AnimTrackQuaternion(SubclassBaseFile):
    ResourceType = 0x8BDB6032
    ParentResourceType = _AnimTrackValue.ResourceType
    parent: _AnimTrackValue
