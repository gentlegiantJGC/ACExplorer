from pyUbiForge2.api.game import SubclassBaseFile
from .Clip import Clip as _Clip


class SendEventClip(SubclassBaseFile):
    ResourceType = 0xE425EE6C
    ParentResourceType = _Clip.ResourceType
    parent: _Clip

