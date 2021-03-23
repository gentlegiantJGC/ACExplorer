from pyUbiForge2.api.game import SubclassBaseFile
from .CameraEvent import CameraEvent as _CameraEvent


class AnimusDeactivationEvent(SubclassBaseFile):
    ResourceType = 0xD0095304
    ParentResourceType = _CameraEvent.ResourceType
    parent: _CameraEvent
