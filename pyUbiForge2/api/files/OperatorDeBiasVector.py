from pyUbiForge2.api.game import SubclassBaseFile
from .Operator import Operator as _Operator


class OperatorDeBiasVector(SubclassBaseFile):
    ResourceType = 0x82859C8C
    ParentResourceType = _Operator.ResourceType
    parent: _Operator

