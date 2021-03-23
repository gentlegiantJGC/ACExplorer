from pyUbiForge2.api.game import SubclassBaseFile
from .SoftBodyInstance import SoftBodyInstance as _SoftBodyInstance


class ClothInstance(SubclassBaseFile):
    ResourceType = 0x273AF22F
    ParentResourceType = _SoftBodyInstance.ResourceType
    parent: _SoftBodyInstance
