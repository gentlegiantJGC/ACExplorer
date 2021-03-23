from pyUbiForge2.api.game import SubclassBaseFile
from .CameraActivator import CameraActivator as _CameraActivator


class ForcedPositionDebugCameraActivator(SubclassBaseFile):
    ResourceType = 0x176C37CB
    ParentResourceType = _CameraActivator.ResourceType
    parent: _CameraActivator
