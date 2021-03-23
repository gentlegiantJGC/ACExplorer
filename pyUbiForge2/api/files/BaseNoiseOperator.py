from pyUbiForge2.api.game import SubclassBaseFile
from .Operator import Operator as _Operator


class BaseNoiseOperator(SubclassBaseFile):
    ResourceType = 0xBEAF6F18
    ParentResourceType = _Operator.ResourceType
    parent: _Operator

