from pyUbiForge2.api.game import SubclassBaseFile
from .Clip import Clip as _Clip


class FactionStatusClip(SubclassBaseFile):
    ResourceType = 0xE7F72BC5
    ParentResourceType = _Clip.ResourceType
    parent: _Clip

