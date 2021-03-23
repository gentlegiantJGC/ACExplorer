from pyUbiForge2.api.game import SubclassBaseFile
from .DLCAddon import DLCAddon as _DLCAddon


class MenuManagerDLCAddon(SubclassBaseFile):
    ResourceType = 0xB583099D
    ParentResourceType = _DLCAddon.ResourceType
    parent: _DLCAddon

