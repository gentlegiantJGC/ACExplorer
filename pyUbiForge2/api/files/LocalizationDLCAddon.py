from pyUbiForge2.api.game import SubclassBaseFile
from .DLCAddon import DLCAddon as _DLCAddon


class LocalizationDLCAddon(SubclassBaseFile):
    ResourceType = 0xB05A1078
    ParentResourceType = _DLCAddon.ResourceType
    parent: _DLCAddon

