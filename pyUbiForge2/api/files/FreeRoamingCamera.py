from pyUbiForge2.api.game import SubclassBaseFile
from .ThirdPersonCamera import ThirdPersonCamera as _ThirdPersonCamera


class FreeRoamingCamera(SubclassBaseFile):
    ResourceType = 0x620DA5E1
    ParentResourceType = _ThirdPersonCamera.ResourceType
    parent: _ThirdPersonCamera

