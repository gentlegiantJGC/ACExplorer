from pyUbiForge2.api.game import SubclassBaseFile
from .Clip import Clip as _Clip


class RHPAfsClip(SubclassBaseFile):
    ResourceType = 0xC0F2000A
    ParentResourceType = _Clip.ResourceType
    parent: _Clip

