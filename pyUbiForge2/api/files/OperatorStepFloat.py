from pyUbiForge2.api.game import SubclassBaseFile
from .Operator import Operator as _Operator


class OperatorStepFloat(SubclassBaseFile):
    ResourceType = 0x4D631CD8
    ParentResourceType = _Operator.ResourceType
    parent: _Operator

