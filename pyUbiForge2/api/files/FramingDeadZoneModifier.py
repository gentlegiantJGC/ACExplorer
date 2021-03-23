from pyUbiForge2.api.game import SubclassBaseFile
from .CameraModifier import CameraModifier as _CameraModifier


class FramingDeadZoneModifier(SubclassBaseFile):
    ResourceType = 0x8D114D4A
    ParentResourceType = _CameraModifier.ResourceType
    parent: _CameraModifier

