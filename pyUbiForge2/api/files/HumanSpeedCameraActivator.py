from pyUbiForge2.api.game import SubclassBaseFile
from .CameraActivator import CameraActivator as _CameraActivator


class HumanSpeedCameraActivator(SubclassBaseFile):
    ResourceType = 0xD2807C71
    ParentResourceType = _CameraActivator.ResourceType
    parent: _CameraActivator
