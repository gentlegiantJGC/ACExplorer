from pyUbiForge2.api.game import SubclassBaseFile
from .CameraModifier import CameraModifier as _CameraModifier


class FreeRoamingModifier(SubclassBaseFile):
    ResourceType = 0x70A32E1C
    ParentResourceType = _CameraModifier.ResourceType
    parent: _CameraModifier

