from pyUbiForge2.api.game import SubclassBaseFile
from .CameraActivator import CameraActivator as _CameraActivator


class GroupTargetingCameraActivator(SubclassBaseFile):
    ResourceType = 0x53B8C257
    ParentResourceType = _CameraActivator.ResourceType
    parent: _CameraActivator

