from pyUbiForge2.api.game import SubclassBaseFile
from .FirstPersonCameraSettings import FirstPersonCameraSettings as _FirstPersonCameraSettings


class AssassinFirstPersonCameraSettings(SubclassBaseFile):
    ResourceType = 0xE649EC90
    ParentResourceType = _FirstPersonCameraSettings.ResourceType
    parent: _FirstPersonCameraSettings

