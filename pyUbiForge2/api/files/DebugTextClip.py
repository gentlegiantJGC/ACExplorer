from pyUbiForge2.api.game import SubclassBaseFile
from .Clip import Clip as _Clip


class DebugTextClip(SubclassBaseFile):
    ResourceType = 0x2DFC1877
    ParentResourceType = _Clip.ResourceType
    parent: _Clip

