from pyUbiForge2.api.game import SubclassBaseFile
from .SoftBodyLOD import SoftBodyLOD as _SoftBodyLOD


class ClothLOD(SubclassBaseFile):
    ResourceType = 0xFA94BA7D
    ParentResourceType = _SoftBodyLOD.ResourceType
    parent: _SoftBodyLOD
