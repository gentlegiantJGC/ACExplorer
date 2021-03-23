from pyUbiForge2.api.game import SubclassBaseFile
from .CameraActivator import CameraActivator as _CameraActivator


class HighProfilCameraActivator(SubclassBaseFile):
    ResourceType = 0x798CA4D3
    ParentResourceType = _CameraActivator.ResourceType
    parent: _CameraActivator

