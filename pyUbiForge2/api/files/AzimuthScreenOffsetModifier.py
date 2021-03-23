from pyUbiForge2.api.game import SubclassBaseFile
from .CameraModifier import CameraModifier as _CameraModifier


class AzimuthScreenOffsetModifier(SubclassBaseFile):
    ResourceType = 0xDAF35D61
    ParentResourceType = _CameraModifier.ResourceType
    parent: _CameraModifier
