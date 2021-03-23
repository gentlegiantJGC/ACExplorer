from pyUbiForge2.api.game import SubclassBaseFile
from .CameraModifier import CameraModifier as _CameraModifier


class TrajectoryModifier(SubclassBaseFile):
    ResourceType = 0x3C7D852C
    ParentResourceType = _CameraModifier.ResourceType
    parent: _CameraModifier
