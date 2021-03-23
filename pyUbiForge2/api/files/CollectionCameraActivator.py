from pyUbiForge2.api.game import SubclassBaseFile
from .CameraActivator import CameraActivator as _CameraActivator


class CollectionCameraActivator(SubclassBaseFile):
    ResourceType = 0x415A8C2B
    ParentResourceType = _CameraActivator.ResourceType
    parent: _CameraActivator

