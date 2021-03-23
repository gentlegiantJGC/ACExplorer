from pyUbiForge2.api.game import SubclassBaseFile
from .PolarCameraSettings import PolarCameraSettings as _PolarCameraSettings


class NavigationCameraSettings(SubclassBaseFile):
    ResourceType = 0x388AD28A
    ParentResourceType = _PolarCameraSettings.ResourceType
    parent: _PolarCameraSettings
