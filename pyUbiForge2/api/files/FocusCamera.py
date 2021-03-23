from pyUbiForge2.api.game import SubclassBaseFile
from .PointOfInterestCamera import PointOfInterestCamera as _PointOfInterestCamera


class FocusCamera(SubclassBaseFile):
    ResourceType = 0xA43A9F0E
    ParentResourceType = _PointOfInterestCamera.ResourceType
    parent: _PointOfInterestCamera
