from pyUbiForge2.api.game import SubclassBaseFile
from .AnimTrackQuaternion import AnimTrackQuaternion as _AnimTrackQuaternion


class AnimTrackQuat32(SubclassBaseFile):
    ResourceType = 0x6026C59F
    ParentResourceType = _AnimTrackQuaternion.ResourceType
    parent: _AnimTrackQuaternion
