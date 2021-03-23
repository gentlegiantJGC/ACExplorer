from pyUbiForge2.api.game import SubclassBaseFile
from .CameraModifier import CameraModifier as _CameraModifier


class AC2HighProfileModifier(SubclassBaseFile):
    ResourceType = 0x222915F9
    ParentResourceType = _CameraModifier.ResourceType
    parent: _CameraModifier
