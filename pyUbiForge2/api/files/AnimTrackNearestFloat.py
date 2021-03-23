from pyUbiForge2.api.game import SubclassBaseFile
from .AnimTrackFloat import AnimTrackFloat as _AnimTrackFloat


class AnimTrackNearestFloat(SubclassBaseFile):
    ResourceType = 0x3D29DB47
    ParentResourceType = _AnimTrackFloat.ResourceType
    parent: _AnimTrackFloat

