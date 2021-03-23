from pyUbiForge2.api.game import SubclassBaseFile
from .PolarCamera import PolarCamera as _PolarCamera


class ThirdPersonCamera(SubclassBaseFile):
    ResourceType = 0x32FFA863
    ParentResourceType = _PolarCamera.ResourceType
    parent: _PolarCamera

