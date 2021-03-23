from pyUbiForge2.api.game import SubclassBaseFile
from .CameraModifier import CameraModifier as _CameraModifier


class TargetMovementCompensationModifier(SubclassBaseFile):
    ResourceType = 0x2B192B0C
    ParentResourceType = _CameraModifier.ResourceType
    parent: _CameraModifier

