from pyUbiForge2.api.game import SubclassBaseFile
from .Clip import Clip as _Clip


class FlythroughClip(SubclassBaseFile):
    ResourceType = 0x308AB956
    ParentResourceType = _Clip.ResourceType
    parent: _Clip

