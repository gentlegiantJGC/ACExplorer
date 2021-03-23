from pyUbiForge2.api.game import SubclassBaseFile
from .DLCAddon import DLCAddon as _DLCAddon


class SoundPackagesDLCAddon(SubclassBaseFile):
    ResourceType = 0x01FFF6FB
    ParentResourceType = _DLCAddon.ResourceType
    parent: _DLCAddon
