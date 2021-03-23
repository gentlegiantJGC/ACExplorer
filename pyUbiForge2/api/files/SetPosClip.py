from pyUbiForge2.api.game import SubclassBaseFile
from .Clip import Clip as _Clip


class SetPosClip(SubclassBaseFile):
    ResourceType = 0xC714A4DE
    ParentResourceType = _Clip.ResourceType
    parent: _Clip

