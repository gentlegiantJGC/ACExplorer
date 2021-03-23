from pyUbiForge2.api.game import SubclassBaseFile
from .Clip import Clip as _Clip


class ToggleAliveBodyHurtStateClip(SubclassBaseFile):
    ResourceType = 0xFCC94600
    ParentResourceType = _Clip.ResourceType
    parent: _Clip

