from pyUbiForge2.api.game import SubclassBaseFile
from .Clip import Clip as _Clip


class SaveGameClip(SubclassBaseFile):
    ResourceType = 0x8BBE3A06
    ParentResourceType = _Clip.ResourceType
    parent: _Clip

