from pyUbiForge2.api.game import SubclassBaseFile
from .CameraEvent import CameraEvent as _CameraEvent


class DebugCameraToggleEvent(SubclassBaseFile):
    ResourceType = 0x11864535
    ParentResourceType = _CameraEvent.ResourceType
    parent: _CameraEvent

