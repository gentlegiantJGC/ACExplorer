from pyUbiForge2.api.game import SubclassBaseFile
from .TargetEulerCamera import TargetEulerCamera as _TargetEulerCamera


class FirstPersonCamera(SubclassBaseFile):
    ResourceType = 0xEC644E55
    ParentResourceType = _TargetEulerCamera.ResourceType
    parent: _TargetEulerCamera
