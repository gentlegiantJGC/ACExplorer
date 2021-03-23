from pyUbiForge2.api.game import SubclassBaseFile
from .CameraModifier import CameraModifier as _CameraModifier


class TargetFramingModifier(SubclassBaseFile):
    ResourceType = 0x4DDED612
    ParentResourceType = _CameraModifier.ResourceType
    parent: _CameraModifier

