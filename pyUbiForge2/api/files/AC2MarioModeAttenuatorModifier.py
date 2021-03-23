from pyUbiForge2.api.game import SubclassBaseFile
from .CameraModifier import CameraModifier as _CameraModifier


class AC2MarioModeAttenuatorModifier(SubclassBaseFile):
    ResourceType = 0xEC0F3BB6
    ParentResourceType = _CameraModifier.ResourceType
    parent: _CameraModifier

