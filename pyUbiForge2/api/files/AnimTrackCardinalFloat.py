from pyUbiForge2.api.game import SubclassBaseFile
from .AnimTrackFloat import AnimTrackFloat as _AnimTrackFloat


class AnimTrackCardinalFloat(SubclassBaseFile):
    ResourceType = 0x02D5BEA6
    ParentResourceType = _AnimTrackFloat.ResourceType
    parent: _AnimTrackFloat
