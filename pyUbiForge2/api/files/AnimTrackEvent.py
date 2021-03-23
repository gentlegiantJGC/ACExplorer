from pyUbiForge2.api.game import SubclassBaseFile
from .AnimTrack import AnimTrack as _AnimTrack


class AnimTrackEvent(SubclassBaseFile):
    ResourceType = 0x41682213
    ParentResourceType = _AnimTrack.ResourceType
    parent: _AnimTrack

