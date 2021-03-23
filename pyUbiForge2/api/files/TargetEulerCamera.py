from pyUbiForge2.api.game import SubclassBaseFile
from .TargetCamera import TargetCamera as _TargetCamera


class TargetEulerCamera(SubclassBaseFile):
    ResourceType = 0x77250773
    ParentResourceType = _TargetCamera.ResourceType
    parent: _TargetCamera

