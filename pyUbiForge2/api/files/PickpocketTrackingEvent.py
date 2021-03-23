from pyUbiForge2.api.game import SubclassBaseFile
from .CameraEvent import CameraEvent as _CameraEvent


class PickpocketTrackingEvent(SubclassBaseFile):
    ResourceType = 0x7E69A3D1
    ParentResourceType = _CameraEvent.ResourceType
    parent: _CameraEvent

