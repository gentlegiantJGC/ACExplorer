from pyUbiForge2.api.game import SubclassBaseFile
from .Camera2 import Camera2 as _Camera2


class SplineCamera2(SubclassBaseFile):
    ResourceType = 0xDCBDF3EB
    ParentResourceType = _Camera2.ResourceType
    parent: _Camera2

