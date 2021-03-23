from pyUbiForge2.api.game import SubclassBaseFile
from .Camera2 import Camera2 as _Camera2


class NullCamera(SubclassBaseFile):
    ResourceType = 0x9FED000A
    ParentResourceType = _Camera2.ResourceType
    parent: _Camera2
