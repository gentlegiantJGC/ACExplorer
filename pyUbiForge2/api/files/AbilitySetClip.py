from pyUbiForge2.api.game import SubclassBaseFile
from .Clip import Clip as _Clip


class AbilitySetClip(SubclassBaseFile):
    ResourceType = 0xD5352A62
    ParentResourceType = _Clip.ResourceType
    parent: _Clip

