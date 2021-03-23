from pyUbiForge2.api.game import SubclassBaseFile
from .SplineCamera import SplineCamera as _SplineCamera


class SplineAxisCamera(SubclassBaseFile):
    ResourceType = 0x618D9054
    ParentResourceType = _SplineCamera.ResourceType
    parent: _SplineCamera
