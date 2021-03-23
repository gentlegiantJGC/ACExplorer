from pyUbiForge2.api.game import SubclassBaseFile
from .FirstPersonCameraSettings import FirstPersonCameraSettings as _FirstPersonCameraSettings


class EavesdroppingCameraSettings(SubclassBaseFile):
    ResourceType = 0x38C56609
    ParentResourceType = _FirstPersonCameraSettings.ResourceType
    parent: _FirstPersonCameraSettings

