from pyUbiForge2.api.game import SubclassBaseFile
from .Operator import Operator as _Operator


class MeshSource(SubclassBaseFile):
    ResourceType = 0xED586F9A
    ParentResourceType = _Operator.ResourceType
    parent: _Operator
