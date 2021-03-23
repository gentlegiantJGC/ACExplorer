from pyUbiForge2.api.game import SubclassBaseFile
from .CameraActivator import CameraActivator as _CameraActivator


class EventBasedActivator(SubclassBaseFile):
    ResourceType = 0xFF103AE9
    ParentResourceType = _CameraActivator.ResourceType
    parent: _CameraActivator
