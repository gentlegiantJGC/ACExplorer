from pyUbiForge2.api.game import SubclassBaseFile
from .PolarCamera import PolarCamera as _PolarCamera


class NavigationCamera(SubclassBaseFile):
    ResourceType = 0x1F8BEC17
    ParentResourceType = _PolarCamera.ResourceType
    parent: _PolarCamera
