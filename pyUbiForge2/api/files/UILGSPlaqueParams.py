from pyUbiForge2.api.game import SubclassBaseFile
from .UIVillaTrophyParams import UIVillaTrophyParams as _UIVillaTrophyParams


class UILGSPlaqueParams(SubclassBaseFile):
    ResourceType = 0x20BF7D70
    ParentResourceType = _UIVillaTrophyParams.ResourceType
    parent: _UIVillaTrophyParams

