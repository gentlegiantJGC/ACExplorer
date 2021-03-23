from pyUbiForge2.api.game import SubclassBaseFile
from .AnimTrackQuaternion import AnimTrackQuaternion as _AnimTrackQuaternion


class AnimTrackQuat24(SubclassBaseFile):
    ResourceType = 0x905E51EB
    ParentResourceType = _AnimTrackQuaternion.ResourceType
    parent: _AnimTrackQuaternion

