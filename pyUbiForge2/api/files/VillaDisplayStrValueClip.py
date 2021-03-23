from pyUbiForge2.api.game import SubclassBaseFile
from .Clip import Clip as _Clip


class VillaDisplayStrValueClip(SubclassBaseFile):
    ResourceType = 0x9792AADE
    ParentResourceType = _Clip.ResourceType
    parent: _Clip
