from pyUbiForge2.api.game import SubclassBaseFile
from .Operator import Operator as _Operator


class OperatorReciprocalVector(SubclassBaseFile):
    ResourceType = 0xA2364ECC
    ParentResourceType = _Operator.ResourceType
    parent: _Operator
