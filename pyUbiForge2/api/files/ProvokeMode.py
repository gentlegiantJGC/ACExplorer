from pyUbiForge2.api.game import SubclassBaseFile
from .ConfrontationMode import ConfrontationMode as _ConfrontationMode


class ProvokeMode(SubclassBaseFile):
    ResourceType = 0x50C3E32E
    ParentResourceType = _ConfrontationMode.ResourceType
    parent: _ConfrontationMode

