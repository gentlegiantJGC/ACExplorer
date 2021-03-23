from pyUbiForge2.api.game import SubclassBaseFile
from .ICameraParameterAnimation import ICameraParameterAnimation as _ICameraParameterAnimation


class CameraParameterAnimationFloat(SubclassBaseFile):
    ResourceType = 0xE415D4E9
    ParentResourceType = _ICameraParameterAnimation.ResourceType
    parent: _ICameraParameterAnimation

