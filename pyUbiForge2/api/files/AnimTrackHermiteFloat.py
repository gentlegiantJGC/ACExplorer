from pyUbiForge2.api.game import SubclassBaseFile
from .AnimTrackFloat import AnimTrackFloat as _AnimTrackFloat


class AnimTrackHermiteFloat(SubclassBaseFile):
    ResourceType = 0x37763313
    ParentResourceType = _AnimTrackFloat.ResourceType
    parent: _AnimTrackFloat

