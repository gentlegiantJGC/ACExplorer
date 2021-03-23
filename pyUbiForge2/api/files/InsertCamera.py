from pyUbiForge2.api.game import SubclassBaseFile
from .ThirdPersonCamera import ThirdPersonCamera as _ThirdPersonCamera


class InsertCamera(SubclassBaseFile):
    ResourceType = 0xA4172405
    ParentResourceType = _ThirdPersonCamera.ResourceType
    parent: _ThirdPersonCamera

