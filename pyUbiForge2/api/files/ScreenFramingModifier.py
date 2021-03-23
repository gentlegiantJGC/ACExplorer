from pyUbiForge2.api.game import SubclassBaseFile
from .CameraModifier import CameraModifier as _CameraModifier


class ScreenFramingModifier(SubclassBaseFile):
    ResourceType = 0xF9B7C9F7
    ParentResourceType = _CameraModifier.ResourceType
    parent: _CameraModifier
