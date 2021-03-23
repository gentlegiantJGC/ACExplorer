from pyUbiForge2.api.game import SubclassBaseFile
from .SplineCamera import SplineCamera as _SplineCamera


class SplinePointAxisCamera(SubclassBaseFile):
    ResourceType = 0x58F2417B
    ParentResourceType = _SplineCamera.ResourceType
    parent: _SplineCamera
