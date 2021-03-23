from pyUbiForge2.api.game import SubclassBaseFile
from .Clip import Clip as _Clip


class TimedClip(SubclassBaseFile):
    ResourceType = 0xF4AFB940
    ParentResourceType = _Clip.ResourceType
    parent: _Clip
