from pyUbiForge2.api.game import SubclassBaseFile
from .CameraEvent import CameraEvent as _CameraEvent


class TargetingCameraStateEvent(SubclassBaseFile):
    ResourceType = 0x01025425
    ParentResourceType = _CameraEvent.ResourceType
    parent: _CameraEvent

