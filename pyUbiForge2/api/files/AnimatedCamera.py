from pyUbiForge2.api.game import SubclassBaseFile
from .Camera import Camera as _Camera


class AnimatedCamera(SubclassBaseFile):
    ResourceType = 0x2E494526
    ParentResourceType = _Camera.ResourceType
    parent: _Camera
