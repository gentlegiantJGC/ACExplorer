from pyUbiForge2.api.game import SubclassBaseFile
from .CameraActivator import CameraActivator as _CameraActivator


class AlwaysActiveCameraActivator(SubclassBaseFile):
    ResourceType = 0x7DFBC960
    ParentResourceType = _CameraActivator.ResourceType
    parent: _CameraActivator

