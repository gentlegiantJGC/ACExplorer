from pyUbiForge2.api.game import SubclassBaseFile
from .ICameraParameterAnimation import (
    ICameraParameterAnimation as _ICameraParameterAnimation,
)


class CameraParameterAnimationVector4(SubclassBaseFile):
    ResourceType = 0x81F38C78
    ParentResourceType = _ICameraParameterAnimation.ResourceType
    parent: _ICameraParameterAnimation
