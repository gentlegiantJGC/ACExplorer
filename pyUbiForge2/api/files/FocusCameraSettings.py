from pyUbiForge2.api.game import SubclassBaseFile
from .PointOfInterestCameraSettings import PointOfInterestCameraSettings as _PointOfInterestCameraSettings


class FocusCameraSettings(SubclassBaseFile):
    ResourceType = 0x307FCBE9
    ParentResourceType = _PointOfInterestCameraSettings.ResourceType
    parent: _PointOfInterestCameraSettings

