from pyUbiForge2.api.game import SubclassBaseFile
from .AnimTrackQuaternion import AnimTrackQuaternion as _AnimTrackQuaternion


class AnimTrackQuatZFloat8(SubclassBaseFile):
    ResourceType = 0x1684969E
    ParentResourceType = _AnimTrackQuaternion.ResourceType
    parent: _AnimTrackQuaternion
