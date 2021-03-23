from pyUbiForge2.api.game import SubclassBaseFile
from .SweetCameraSettings import SweetCameraSettings as _SweetCameraSettings


class FightCameraSettings(SubclassBaseFile):
    ResourceType = 0x3967237E
    ParentResourceType = _SweetCameraSettings.ResourceType
    parent: _SweetCameraSettings

