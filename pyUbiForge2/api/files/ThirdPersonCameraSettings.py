from pyUbiForge2.api.game import SubclassBaseFile
from .PolarCameraSettings import PolarCameraSettings as _PolarCameraSettings


class ThirdPersonCameraSettings(SubclassBaseFile):
    ResourceType = 0x0936B8E8
    ParentResourceType = _PolarCameraSettings.ResourceType
    parent: _PolarCameraSettings

