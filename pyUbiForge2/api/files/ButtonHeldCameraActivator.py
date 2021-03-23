from pyUbiForge2.api.game import SubclassBaseFile
from .CameraActivator import CameraActivator as _CameraActivator


class ButtonHeldCameraActivator(SubclassBaseFile):
    ResourceType = 0x984BF1FF
    ParentResourceType = _CameraActivator.ResourceType
    parent: _CameraActivator

