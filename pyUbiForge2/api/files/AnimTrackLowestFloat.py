from pyUbiForge2.api.game import SubclassBaseFile
from .AnimTrackFloat import AnimTrackFloat as _AnimTrackFloat


class AnimTrackLowestFloat(SubclassBaseFile):
    ResourceType = 0xE4B3803A
    ParentResourceType = _AnimTrackFloat.ResourceType
    parent: _AnimTrackFloat

