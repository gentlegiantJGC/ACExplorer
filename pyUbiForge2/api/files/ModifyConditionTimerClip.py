from pyUbiForge2.api.game import SubclassBaseFile
from .Clip import Clip as _Clip


class ModifyConditionTimerClip(SubclassBaseFile):
    ResourceType = 0x2C1393F3
    ParentResourceType = _Clip.ResourceType
    parent: _Clip
