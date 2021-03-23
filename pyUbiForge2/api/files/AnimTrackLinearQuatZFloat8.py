from pyUbiForge2.api.game import SubclassBaseFile
from .AnimTrackQuatZFloat8 import AnimTrackQuatZFloat8 as _AnimTrackQuatZFloat8


class AnimTrackLinearQuatZFloat8(SubclassBaseFile):
    ResourceType = 0xADA11722
    ParentResourceType = _AnimTrackQuatZFloat8.ResourceType
    parent: _AnimTrackQuatZFloat8

