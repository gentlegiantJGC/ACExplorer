from pyUbiForge2.api.game import SubclassBaseFile
from .TargetEulerCamera import TargetEulerCamera as _TargetEulerCamera


class SplineCamera(SubclassBaseFile):
    ResourceType = 0x6494543A
    ParentResourceType = _TargetEulerCamera.ResourceType
    parent: _TargetEulerCamera

