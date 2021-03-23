from pyUbiForge2.api.game import SubclassBaseFile
from .Clip import Clip as _Clip


class CrowdCompositionClip(SubclassBaseFile):
    ResourceType = 0xA61632B9
    ParentResourceType = _Clip.ResourceType
    parent: _Clip

