from pyUbiForge2.api.game import SubclassBaseFile
from .Operator import Operator as _Operator


class LightingOperator(SubclassBaseFile):
    ResourceType = 0x5C40C017
    ParentResourceType = _Operator.ResourceType
    parent: _Operator

