from pyUbiForge2.api.game import SubclassBaseFile
from .CameraModifier import CameraModifier as _CameraModifier


class TargetFramingAttenuatorModifier(SubclassBaseFile):
    ResourceType = 0xB37232D7
    ParentResourceType = _CameraModifier.ResourceType
    parent: _CameraModifier
