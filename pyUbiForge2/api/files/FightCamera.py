from pyUbiForge2.api.game import SubclassBaseFile
from .SweetCamera import SweetCamera as _SweetCamera


class FightCamera(SubclassBaseFile):
    ResourceType = 0xD6D1A431
    ParentResourceType = _SweetCamera.ResourceType
    parent: _SweetCamera
