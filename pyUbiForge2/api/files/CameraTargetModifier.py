from pyUbiForge2.api.game import SubclassBaseFile
from .CameraModifier import CameraModifier as _CameraModifier


class CameraTargetModifier(SubclassBaseFile):
    ResourceType = 0xE8F43ADF
    ParentResourceType = _CameraModifier.ResourceType
    parent: _CameraModifier
