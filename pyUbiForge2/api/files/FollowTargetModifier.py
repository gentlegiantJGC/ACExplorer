from pyUbiForge2.api.game import SubclassBaseFile
from .CameraModifier import CameraModifier as _CameraModifier


class FollowTargetModifier(SubclassBaseFile):
    ResourceType = 0x5012F910
    ParentResourceType = _CameraModifier.ResourceType
    parent: _CameraModifier

