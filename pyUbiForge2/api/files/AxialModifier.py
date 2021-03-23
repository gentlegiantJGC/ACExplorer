from pyUbiForge2.api.game import SubclassBaseFile
from .CameraModifier import CameraModifier as _CameraModifier


class AxialModifier(SubclassBaseFile):
    ResourceType = 0xD5292827
    ParentResourceType = _CameraModifier.ResourceType
    parent: _CameraModifier

