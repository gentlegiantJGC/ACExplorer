from pyUbiForge2.api.game import SubclassBaseFile
from .ConfrontationMode import ConfrontationMode as _ConfrontationMode


class SneakoutMode(SubclassBaseFile):
    ResourceType = 0xFF3AC46B
    ParentResourceType = _ConfrontationMode.ResourceType
    parent: _ConfrontationMode
