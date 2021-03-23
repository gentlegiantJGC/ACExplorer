from pyUbiForge2.api.game import SubclassBaseFile
from .CameraModifier import CameraModifier as _CameraModifier


class TargetLeadingModifier(SubclassBaseFile):
    ResourceType = 0xB4070739
    ParentResourceType = _CameraModifier.ResourceType
    parent: _CameraModifier

