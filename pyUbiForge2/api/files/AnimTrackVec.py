from pyUbiForge2.api.game import SubclassBaseFile
from .AnimTrackValue import AnimTrackValue as _AnimTrackValue


class AnimTrackVec(SubclassBaseFile):
    ResourceType = 0xADE9A9DB
    ParentResourceType = _AnimTrackValue.ResourceType
    parent: _AnimTrackValue
