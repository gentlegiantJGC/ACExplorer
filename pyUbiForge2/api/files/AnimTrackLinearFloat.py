from pyUbiForge2.api.game import SubclassBaseFile
from .AnimTrackFloat import AnimTrackFloat as _AnimTrackFloat


class AnimTrackLinearFloat(SubclassBaseFile):
    ResourceType = 0xCFD66AAD
    ParentResourceType = _AnimTrackFloat.ResourceType
    parent: _AnimTrackFloat
