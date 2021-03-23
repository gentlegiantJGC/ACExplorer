from pyUbiForge2.api.game import SubclassBaseFile
from .Camera2 import Camera2 as _Camera2


class MovementCompensationCamera(SubclassBaseFile):
    ResourceType = 0xD555BD2A
    ParentResourceType = _Camera2.ResourceType
    parent: _Camera2

