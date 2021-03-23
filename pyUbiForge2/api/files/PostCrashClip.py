from pyUbiForge2.api.game import SubclassBaseFile
from .Clip import Clip as _Clip


class PostCrashClip(SubclassBaseFile):
    ResourceType = 0xE8535A42
    ParentResourceType = _Clip.ResourceType
    parent: _Clip

