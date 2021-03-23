from pyUbiForge2.api.game import SubclassBaseFile
from .CameraActivator import CameraActivator as _CameraActivator


class NavigationCameraActivator(SubclassBaseFile):
    ResourceType = 0xD8893D35
    ParentResourceType = _CameraActivator.ResourceType
    parent: _CameraActivator

