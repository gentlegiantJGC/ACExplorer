from pyUbiForge2.api.game import SubclassBaseFile
from .Operator import Operator as _Operator


class OperatorNormalize(SubclassBaseFile):
    ResourceType = 0x98E64348
    ParentResourceType = _Operator.ResourceType
    parent: _Operator

