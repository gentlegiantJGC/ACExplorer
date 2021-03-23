from pyUbiForge2.api.game import SubclassBaseFile
from .Operator import Operator as _Operator


class OperatorFresnelFactor(SubclassBaseFile):
    ResourceType = 0xBF25E975
    ParentResourceType = _Operator.ResourceType
    parent: _Operator
