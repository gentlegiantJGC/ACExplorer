from pyUbiForge2.api.game import SubclassBaseFile
from .TargetEulerCamera import TargetEulerCamera as _TargetEulerCamera


class FixedCamera(SubclassBaseFile):
    ResourceType = 0x5973A08E
    ParentResourceType = _TargetEulerCamera.ResourceType
    parent: _TargetEulerCamera

