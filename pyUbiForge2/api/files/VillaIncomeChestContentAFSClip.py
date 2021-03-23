from pyUbiForge2.api.game import SubclassBaseFile
from .Clip import Clip as _Clip


class VillaIncomeChestContentAFSClip(SubclassBaseFile):
    ResourceType = 0xFE8DF8C2
    ParentResourceType = _Clip.ResourceType
    parent: _Clip

