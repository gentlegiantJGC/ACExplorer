from pyUbiForge2.api.game import SubclassBaseFile
from .Operator import Operator as _Operator


class CustomOperator(SubclassBaseFile):
    ResourceType = 0x90A535BF
    ParentResourceType = _Operator.ResourceType
    parent: _Operator

