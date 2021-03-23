from pyUbiForge2.api.game import SubclassBaseFile
from .Camera2 import Camera2 as _Camera2


class AC2FirstPersonCamera(SubclassBaseFile):
    ResourceType = 0xE2AE5A1F
    ParentResourceType = _Camera2.ResourceType
    parent: _Camera2
