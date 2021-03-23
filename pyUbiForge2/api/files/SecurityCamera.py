from pyUbiForge2.api.game import SubclassBaseFile
from .ThirdPersonCamera import ThirdPersonCamera as _ThirdPersonCamera


class SecurityCamera(SubclassBaseFile):
    ResourceType = 0x97509CDD
    ParentResourceType = _ThirdPersonCamera.ResourceType
    parent: _ThirdPersonCamera
