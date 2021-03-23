from pyUbiForge2.api.game import SubclassBaseFile
from .VillaItemSettings import VillaItemSettings as _VillaItemSettings


class VillaCodexPageSettings(SubclassBaseFile):
    ResourceType = 0x77CD3637
    ParentResourceType = _VillaItemSettings.ResourceType
    parent: _VillaItemSettings
