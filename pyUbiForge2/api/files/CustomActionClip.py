from pyUbiForge2.api.game import SubclassBaseFile
from .Clip import Clip as _Clip


class CustomActionClip(SubclassBaseFile):
    ResourceType = 0x224792F5
    ParentResourceType = _Clip.ResourceType
    parent: _Clip

