from pyUbiForge2.api.game import SubclassBaseFile
from .Operator import Operator as _Operator


class ShaderLODOperator(SubclassBaseFile):
    ResourceType = 0x544633D7
    ParentResourceType = _Operator.ResourceType
    parent: _Operator

