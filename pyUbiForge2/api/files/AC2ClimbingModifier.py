from pyUbiForge2.api.game import SubclassBaseFile
from .CameraModifier import CameraModifier as _CameraModifier


class AC2ClimbingModifier(SubclassBaseFile):
    ResourceType = 0xB939B15D
    ParentResourceType = _CameraModifier.ResourceType
    parent: _CameraModifier

