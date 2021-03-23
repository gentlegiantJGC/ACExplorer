from pyUbiForge2.api.game import SubclassBaseFile
from .ThirdPersonCamera import ThirdPersonCamera as _ThirdPersonCamera


class CloseUpCamera(SubclassBaseFile):
    ResourceType = 0x961165F9
    ParentResourceType = _ThirdPersonCamera.ResourceType
    parent: _ThirdPersonCamera

