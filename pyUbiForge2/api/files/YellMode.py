from pyUbiForge2.api.game import SubclassBaseFile
from .ConfrontationMode import ConfrontationMode as _ConfrontationMode


class YellMode(SubclassBaseFile):
    ResourceType = 0xC38D3622
    ParentResourceType = _ConfrontationMode.ResourceType
    parent: _ConfrontationMode
