from pyUbiForge2.api.game import SubclassBaseFile
from .Operator import Operator as _Operator


class MetaOperator(SubclassBaseFile):
    ResourceType = 0x0BD2E0B0
    ParentResourceType = _Operator.ResourceType
    parent: _Operator
