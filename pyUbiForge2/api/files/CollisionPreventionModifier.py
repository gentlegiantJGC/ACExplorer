from pyUbiForge2.api.game import SubclassBaseFile
from .CameraModifier import CameraModifier as _CameraModifier


class CollisionPreventionModifier(SubclassBaseFile):
    ResourceType = 0x79CC93B4
    ParentResourceType = _CameraModifier.ResourceType
    parent: _CameraModifier
