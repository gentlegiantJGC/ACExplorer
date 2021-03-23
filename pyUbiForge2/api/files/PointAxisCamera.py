from pyUbiForge2.api.game import SubclassBaseFile
from .TargetEulerCamera import TargetEulerCamera as _TargetEulerCamera


class PointAxisCamera(SubclassBaseFile):
    ResourceType = 0x20A8A43E
    ParentResourceType = _TargetEulerCamera.ResourceType
    parent: _TargetEulerCamera
