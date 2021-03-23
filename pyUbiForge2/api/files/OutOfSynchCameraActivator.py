from pyUbiForge2.api.game import SubclassBaseFile
from .CameraActivator import CameraActivator as _CameraActivator


class OutOfSynchCameraActivator(SubclassBaseFile):
    ResourceType = 0xC335C221
    ParentResourceType = _CameraActivator.ResourceType
    parent: _CameraActivator

