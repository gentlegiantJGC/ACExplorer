from pyUbiForge2.api.game import SubclassBaseFile
from .Clip import Clip as _Clip


class ConditionTimerClip(SubclassBaseFile):
    ResourceType = 0x4FCFF42B
    ParentResourceType = _Clip.ResourceType
    parent: _Clip
