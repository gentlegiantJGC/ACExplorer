from pyUbiForge2.api.game import SubclassBaseFile
from .SweetCamera import SweetCamera as _SweetCamera


class LedgeCheckCamera(SubclassBaseFile):
    ResourceType = 0x83975875
    ParentResourceType = _SweetCamera.ResourceType
    parent: _SweetCamera
