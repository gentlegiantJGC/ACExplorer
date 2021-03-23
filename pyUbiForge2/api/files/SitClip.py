from pyUbiForge2.api.game import SubclassBaseFile
from .Clip import Clip as _Clip


class SitClip(SubclassBaseFile):
    ResourceType = 0x80AE508C
    ParentResourceType = _Clip.ResourceType
    parent: _Clip

