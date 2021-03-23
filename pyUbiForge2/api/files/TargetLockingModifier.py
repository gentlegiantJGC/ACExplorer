from pyUbiForge2.api.game import SubclassBaseFile
from .CameraModifier import CameraModifier as _CameraModifier


class TargetLockingModifier(SubclassBaseFile):
    ResourceType = 0x74F8F798
    ParentResourceType = _CameraModifier.ResourceType
    parent: _CameraModifier
