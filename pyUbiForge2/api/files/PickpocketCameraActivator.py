from pyUbiForge2.api.game import SubclassBaseFile
from .CameraActivator import CameraActivator as _CameraActivator


class PickpocketCameraActivator(SubclassBaseFile):
    ResourceType = 0xE6A58285
    ParentResourceType = _CameraActivator.ResourceType
    parent: _CameraActivator

