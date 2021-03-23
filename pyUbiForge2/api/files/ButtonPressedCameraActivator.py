from pyUbiForge2.api.game import SubclassBaseFile
from .CameraActivator import CameraActivator as _CameraActivator


class ButtonPressedCameraActivator(SubclassBaseFile):
    ResourceType = 0xDB192154
    ParentResourceType = _CameraActivator.ResourceType
    parent: _CameraActivator

