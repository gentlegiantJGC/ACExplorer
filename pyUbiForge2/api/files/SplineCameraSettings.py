from pyUbiForge2.api.game import SubclassBaseFile
from .TargetEulerCameraSettings import (
    TargetEulerCameraSettings as _TargetEulerCameraSettings,
)


class SplineCameraSettings(SubclassBaseFile):
    ResourceType = 0x35E1C55A
    ParentResourceType = _TargetEulerCameraSettings.ResourceType
    parent: _TargetEulerCameraSettings
