from pyUbiForge2.api.game import SubclassBaseFile
from .ThirdPersonCameraSettings import (
    ThirdPersonCameraSettings as _ThirdPersonCameraSettings,
)


class PointOfInterestCameraSettings(SubclassBaseFile):
    ResourceType = 0x3597B59B
    ParentResourceType = _ThirdPersonCameraSettings.ResourceType
    parent: _ThirdPersonCameraSettings
