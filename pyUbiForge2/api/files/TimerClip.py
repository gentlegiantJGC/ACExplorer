from pyUbiForge2.api.game import SubclassBaseFile
from .Clip import Clip as _Clip


class TimerClip(SubclassBaseFile):
    ResourceType = 0x1B0FDB62
    ParentResourceType = _Clip.ResourceType
    parent: _Clip
