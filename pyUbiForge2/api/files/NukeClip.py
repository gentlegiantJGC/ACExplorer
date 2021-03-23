from pyUbiForge2.api.game import SubclassBaseFile
from .Clip import Clip as _Clip


class NukeClip(SubclassBaseFile):
    ResourceType = 0xF8D293DB
    ParentResourceType = _Clip.ResourceType
    parent: _Clip

