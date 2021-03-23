from pyUbiForge2.api.game import SubclassBaseFile
from .Clip import Clip as _Clip


class VillaUpgradeBuildingClip(SubclassBaseFile):
    ResourceType = 0x0B100313
    ParentResourceType = _Clip.ResourceType
    parent: _Clip
