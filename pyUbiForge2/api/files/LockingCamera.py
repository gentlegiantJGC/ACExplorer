from pyUbiForge2.api.game import SubclassBaseFile
from .Camera2 import Camera2 as _Camera2


class LockingCamera(SubclassBaseFile):
    ResourceType = 0x64762F98
    ParentResourceType = _Camera2.ResourceType
    parent: _Camera2
