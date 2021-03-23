from pyUbiForge2.api.game import SubclassBaseFile
from .Operator import Operator as _Operator


class OperatorStepVector(SubclassBaseFile):
    ResourceType = 0x1387B334
    ParentResourceType = _Operator.ResourceType
    parent: _Operator

