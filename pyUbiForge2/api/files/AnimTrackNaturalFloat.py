from pyUbiForge2.api.game import SubclassBaseFile
from .AnimTrackFloat import AnimTrackFloat as _AnimTrackFloat


class AnimTrackNaturalFloat(SubclassBaseFile):
    ResourceType = 0x41ACBA83
    ParentResourceType = _AnimTrackFloat.ResourceType
    parent: _AnimTrackFloat

