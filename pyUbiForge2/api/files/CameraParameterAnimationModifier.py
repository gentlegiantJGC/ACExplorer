from pyUbiForge2.api.game import SubclassBaseFile
from .CameraModifier import CameraModifier as _CameraModifier


class CameraParameterAnimationModifier(SubclassBaseFile):
    ResourceType = 0xFC598BA9
    ParentResourceType = _CameraModifier.ResourceType
    parent: _CameraModifier
