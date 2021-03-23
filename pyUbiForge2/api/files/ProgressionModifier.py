from pyUbiForge2.api.game import SubclassBaseFile
from .CameraModifier import CameraModifier as _CameraModifier


class ProgressionModifier(SubclassBaseFile):
    ResourceType = 0x6350F02C
    ParentResourceType = _CameraModifier.ResourceType
    parent: _CameraModifier

