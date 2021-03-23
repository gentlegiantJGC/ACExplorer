from pyUbiForge2.api.game import SubclassBaseFile
from .Camera2 import Camera2 as _Camera2


class FPSCamera(SubclassBaseFile):
    ResourceType = 0x81E8245F
    ParentResourceType = _Camera2.ResourceType
    parent: _Camera2

