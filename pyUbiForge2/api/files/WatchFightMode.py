from pyUbiForge2.api.game import SubclassBaseFile
from .ConfrontationMode import ConfrontationMode as _ConfrontationMode


class WatchFightMode(SubclassBaseFile):
    ResourceType = 0xBE265AB0
    ParentResourceType = _ConfrontationMode.ResourceType
    parent: _ConfrontationMode
