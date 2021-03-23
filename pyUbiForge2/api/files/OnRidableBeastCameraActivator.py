from pyUbiForge2.api.game import SubclassBaseFile
from .CameraActivator import CameraActivator as _CameraActivator


class OnRidableBeastCameraActivator(SubclassBaseFile):
    ResourceType = 0xCF673B3C
    ParentResourceType = _CameraActivator.ResourceType
    parent: _CameraActivator
