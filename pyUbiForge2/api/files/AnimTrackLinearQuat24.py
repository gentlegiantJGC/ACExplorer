from pyUbiForge2.api.game import SubclassBaseFile
from .AnimTrackQuat24 import AnimTrackQuat24 as _AnimTrackQuat24


class AnimTrackLinearQuat24(SubclassBaseFile):
    ResourceType = 0x742C2BFC
    ParentResourceType = _AnimTrackQuat24.ResourceType
    parent: _AnimTrackQuat24
