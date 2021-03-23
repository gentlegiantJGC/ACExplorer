from pyUbiForge2.api.game import SubclassBaseFile
from .CameraModifier import CameraModifier as _CameraModifier


class PolarControlsModifier(SubclassBaseFile):
    ResourceType = 0x8C86BA80
    ParentResourceType = _CameraModifier.ResourceType
    parent: _CameraModifier
