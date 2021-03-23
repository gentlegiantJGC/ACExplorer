from pyUbiForge2.api.game import SubclassBaseFile
from .TargetEulerCameraControl import TargetEulerCameraControl as _TargetEulerCameraControl


class PadTargetEulerCameraControl(SubclassBaseFile):
    ResourceType = 0x04EAA180
    ParentResourceType = _TargetEulerCameraControl.ResourceType
    parent: _TargetEulerCameraControl

