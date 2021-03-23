from pyUbiForge2.api.game import SubclassBaseFile
from .Camera2 import Camera2 as _Camera2


class FreeRoamingCamera2(SubclassBaseFile):
    ResourceType = 0xCDBA6146
    ParentResourceType = _Camera2.ResourceType
    parent: _Camera2
