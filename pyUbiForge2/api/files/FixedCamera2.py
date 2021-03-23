from pyUbiForge2.api.game import SubclassBaseFile
from .Camera2 import Camera2 as _Camera2


class FixedCamera2(SubclassBaseFile):
    ResourceType = 0x108C638A
    ParentResourceType = _Camera2.ResourceType
    parent: _Camera2

