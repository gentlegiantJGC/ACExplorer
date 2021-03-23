from pyUbiForge2.api.game import SubclassBaseFile
from .ConfrontationMode import ConfrontationMode as _ConfrontationMode


class ConfrontMode(SubclassBaseFile):
    ResourceType = 0xA4C8B831
    ParentResourceType = _ConfrontationMode.ResourceType
    parent: _ConfrontationMode
