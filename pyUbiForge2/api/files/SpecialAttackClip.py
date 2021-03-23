from pyUbiForge2.api.game import SubclassBaseFile
from .Clip import Clip as _Clip


class SpecialAttackClip(SubclassBaseFile):
    ResourceType = 0x7B66398C
    ParentResourceType = _Clip.ResourceType
    parent: _Clip

