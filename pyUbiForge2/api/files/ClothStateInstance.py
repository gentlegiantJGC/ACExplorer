from pyUbiForge2.api.game import SubclassBaseFile
from .SoftBodyStateInstance import SoftBodyStateInstance as _SoftBodyStateInstance


class ClothStateInstance(SubclassBaseFile):
    ResourceType = 0x6086DC59
    ParentResourceType = _SoftBodyStateInstance.ResourceType
    parent: _SoftBodyStateInstance

