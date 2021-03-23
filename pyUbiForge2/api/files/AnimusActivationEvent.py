from pyUbiForge2.api.game import SubclassBaseFile
from .CameraEvent import CameraEvent as _CameraEvent


class AnimusActivationEvent(SubclassBaseFile):
    ResourceType = 0xAEC68113
    ParentResourceType = _CameraEvent.ResourceType
    parent: _CameraEvent
