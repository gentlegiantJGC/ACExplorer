from pyUbiForge2.api.game import SubclassBaseFile
from .AnimTrackQuaternion import AnimTrackQuaternion as _AnimTrackQuaternion


class AnimTrackQuat(SubclassBaseFile):
    ResourceType = 0x27014116
    ParentResourceType = _AnimTrackQuaternion.ResourceType
    parent: _AnimTrackQuaternion
