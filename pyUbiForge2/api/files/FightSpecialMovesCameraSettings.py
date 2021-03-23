from pyUbiForge2.api.game import SubclassBaseFile
from .InsertCameraSettings import InsertCameraSettings as _InsertCameraSettings


class FightSpecialMovesCameraSettings(SubclassBaseFile):
    ResourceType = 0xBF6278DC
    ParentResourceType = _InsertCameraSettings.ResourceType
    parent: _InsertCameraSettings

