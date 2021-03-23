from pyUbiForge2.api.game import SubclassBaseFile
from .AnimTrackQuatZFloat16 import AnimTrackQuatZFloat16 as _AnimTrackQuatZFloat16


class AnimTrackLinearQuatZFloat16(SubclassBaseFile):
    ResourceType = 0x19B721AE
    ParentResourceType = _AnimTrackQuatZFloat16.ResourceType
    parent: _AnimTrackQuatZFloat16
