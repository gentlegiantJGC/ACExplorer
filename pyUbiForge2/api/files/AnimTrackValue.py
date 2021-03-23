from pyUbiForge2.api.game import SubclassBaseFile
from .AnimTrack import AnimTrack as _AnimTrack


class AnimTrackValue(SubclassBaseFile):
    ResourceType = 0x67B17080
    ParentResourceType = _AnimTrack.ResourceType
    parent: _AnimTrack

