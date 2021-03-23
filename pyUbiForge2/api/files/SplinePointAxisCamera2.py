from pyUbiForge2.api.game import SubclassBaseFile
from .Camera2 import Camera2 as _Camera2


class SplinePointAxisCamera2(SubclassBaseFile):
    ResourceType = 0xDD5AE4F8
    ParentResourceType = _Camera2.ResourceType
    parent: _Camera2

