from pyUbiForge2.api.game import SubclassBaseFile
from .FirstPersonCamera import FirstPersonCamera as _FirstPersonCamera


class AssassinFirstPersonCamera(SubclassBaseFile):
    ResourceType = 0x704D24BB
    ParentResourceType = _FirstPersonCamera.ResourceType
    parent: _FirstPersonCamera
