from pyUbiForge2.api.game import SubclassBaseFile
from .CameraModifier import CameraModifier as _CameraModifier


class BasePositionOrientationModifier(SubclassBaseFile):
    ResourceType = 0xD6FE1362
    ParentResourceType = _CameraModifier.ResourceType
    parent: _CameraModifier
