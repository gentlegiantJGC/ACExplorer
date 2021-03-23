from pyUbiForge2.api.game import SubclassBaseFile
from .CameraModifier import CameraModifier as _CameraModifier


class FreeRoamingCollisionModifier(SubclassBaseFile):
    ResourceType = 0x8D313D22
    ParentResourceType = _CameraModifier.ResourceType
    parent: _CameraModifier
