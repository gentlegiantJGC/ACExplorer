from pyUbiForge2.api.game import SubclassBaseFile
from .CameraEvent import CameraEvent as _CameraEvent


class EavesdroppingDataEvent(SubclassBaseFile):
    ResourceType = 0x0A8D45EC
    ParentResourceType = _CameraEvent.ResourceType
    parent: _CameraEvent

