from pyUbiForge2.api.game import SubclassBaseFile
from .SplineCameraSettings import SplineCameraSettings as _SplineCameraSettings


class SplineAxisCameraSettings(SubclassBaseFile):
    ResourceType = 0x24EB1068
    ParentResourceType = _SplineCameraSettings.ResourceType
    parent: _SplineCameraSettings

