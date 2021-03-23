from pyUbiForge2.api.game import SubclassBaseFile
from .CameraModifier import CameraModifier as _CameraModifier


class MainTargetDampingModifier(SubclassBaseFile):
    ResourceType = 0xDAF42254
    ParentResourceType = _CameraModifier.ResourceType
    parent: _CameraModifier

