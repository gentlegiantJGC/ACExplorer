from pyUbiForge2.api.game import SubclassBaseFile
from .AnimTrackQuaternion import AnimTrackQuaternion as _AnimTrackQuaternion


class AnimTrackQuat48(SubclassBaseFile):
    ResourceType = 0xCFB2BA46
    ParentResourceType = _AnimTrackQuaternion.ResourceType
    parent: _AnimTrackQuaternion
