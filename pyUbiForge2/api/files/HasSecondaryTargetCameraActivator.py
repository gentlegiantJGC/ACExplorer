from pyUbiForge2.api.game import SubclassBaseFile
from .CameraActivator import CameraActivator as _CameraActivator


class HasSecondaryTargetCameraActivator(SubclassBaseFile):
    ResourceType = 0xD502412B
    ParentResourceType = _CameraActivator.ResourceType
    parent: _CameraActivator
