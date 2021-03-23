from pyUbiForge2.api.game import SubclassBaseFile
from .InsertCameraSettings import InsertCameraSettings as _InsertCameraSettings


class AssassinationCameraSettings(SubclassBaseFile):
    ResourceType = 0x7AFF6565
    ParentResourceType = _InsertCameraSettings.ResourceType
    parent: _InsertCameraSettings
