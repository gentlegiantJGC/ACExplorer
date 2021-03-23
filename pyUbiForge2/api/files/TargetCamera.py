from pyUbiForge2.api.game import SubclassBaseFile
from .Camera import Camera as _Camera


class TargetCamera(SubclassBaseFile):
    ResourceType = 0x1212475B
    ParentResourceType = _Camera.ResourceType
    parent: _Camera

