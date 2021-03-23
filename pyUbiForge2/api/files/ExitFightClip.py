from pyUbiForge2.api.game import SubclassBaseFile
from .Clip import Clip as _Clip


class ExitFightClip(SubclassBaseFile):
    ResourceType = 0xB1350264
    ParentResourceType = _Clip.ResourceType
    parent: _Clip
