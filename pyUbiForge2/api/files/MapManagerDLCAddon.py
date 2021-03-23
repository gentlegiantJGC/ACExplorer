from pyUbiForge2.api.game import SubclassBaseFile
from .DLCAddon import DLCAddon as _DLCAddon


class MapManagerDLCAddon(SubclassBaseFile):
    ResourceType = 0x847F8B57
    ParentResourceType = _DLCAddon.ResourceType
    parent: _DLCAddon
