from pyUbiForge2.api.game import SubclassBaseFile
from .ThirdPersonCamera import ThirdPersonCamera as _ThirdPersonCamera


class SweetCamera(SubclassBaseFile):
    ResourceType = 0x85E440B4
    ParentResourceType = _ThirdPersonCamera.ResourceType
    parent: _ThirdPersonCamera

