from pyUbiForge2.api.game import SubclassBaseFile
from .SplineCameraSettings import SplineCameraSettings as _SplineCameraSettings


class SplinePointAxisCameraSettings(SubclassBaseFile):
    ResourceType = 0x5F4C0D80
    ParentResourceType = _SplineCameraSettings.ResourceType
    parent: _SplineCameraSettings
