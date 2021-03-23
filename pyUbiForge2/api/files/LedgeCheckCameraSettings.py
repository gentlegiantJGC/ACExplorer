from pyUbiForge2.api.game import SubclassBaseFile
from .SweetCameraSettings import SweetCameraSettings as _SweetCameraSettings


class LedgeCheckCameraSettings(SubclassBaseFile):
    ResourceType = 0x1E9C160E
    ParentResourceType = _SweetCameraSettings.ResourceType
    parent: _SweetCameraSettings
