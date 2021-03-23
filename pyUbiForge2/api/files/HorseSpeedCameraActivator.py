from pyUbiForge2.api.game import SubclassBaseFile
from .CameraActivator import CameraActivator as _CameraActivator


class HorseSpeedCameraActivator(SubclassBaseFile):
    ResourceType = 0x08E4A66D
    ParentResourceType = _CameraActivator.ResourceType
    parent: _CameraActivator
