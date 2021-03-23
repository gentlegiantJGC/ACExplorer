from pyUbiForge2.api.game import SubclassBaseFile
from .AnimTrackFloat import AnimTrackFloat as _AnimTrackFloat


class AnimTrackHermiteVelFloat(SubclassBaseFile):
    ResourceType = 0x4DD29CD9
    ParentResourceType = _AnimTrackFloat.ResourceType
    parent: _AnimTrackFloat
