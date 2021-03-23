from pyUbiForge2.api.game import SubclassBaseFile
from .CameraActivator import CameraActivator as _CameraActivator


class TimedCameraActivator(SubclassBaseFile):
    ResourceType = 0xAE4C636B
    ParentResourceType = _CameraActivator.ResourceType
    parent: _CameraActivator
