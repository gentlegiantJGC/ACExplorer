from pyUbiForge2.api.game import SubclassBaseFile
from .Clip import Clip as _Clip


class HideCrowdClip(SubclassBaseFile):
    ResourceType = 0xA89565C1
    ParentResourceType = _Clip.ResourceType
    parent: _Clip

