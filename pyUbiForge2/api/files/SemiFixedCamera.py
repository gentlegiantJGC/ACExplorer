from pyUbiForge2.api.game import SubclassBaseFile
from .TargetEulerCamera import TargetEulerCamera as _TargetEulerCamera


class SemiFixedCamera(SubclassBaseFile):
    ResourceType = 0x8E999133
    ParentResourceType = _TargetEulerCamera.ResourceType
    parent: _TargetEulerCamera

