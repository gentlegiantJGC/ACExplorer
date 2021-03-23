from pyUbiForge2.api.game import SubclassBaseFile
from .DLCAddon import DLCAddon as _DLCAddon


class UniverseDLCAddon(SubclassBaseFile):
    ResourceType = 0xA58F3865
    ParentResourceType = _DLCAddon.ResourceType
    parent: _DLCAddon

