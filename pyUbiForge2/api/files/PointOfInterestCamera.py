from pyUbiForge2.api.game import SubclassBaseFile
from .ThirdPersonCamera import ThirdPersonCamera as _ThirdPersonCamera


class PointOfInterestCamera(SubclassBaseFile):
    ResourceType = 0x7FA8C9C4
    ParentResourceType = _ThirdPersonCamera.ResourceType
    parent: _ThirdPersonCamera
