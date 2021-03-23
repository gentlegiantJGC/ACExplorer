from pyUbiForge2.api.game import SubclassBaseFile
from .CameraActivator import CameraActivator as _CameraActivator


class ToleranceCameraActivator(SubclassBaseFile):
    ResourceType = 0x7E5B2799
    ParentResourceType = _CameraActivator.ResourceType
    parent: _CameraActivator
