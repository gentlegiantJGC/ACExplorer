from pyUbiForge2.api.game import SubclassBaseFile
from .Operator import Operator as _Operator


class BaseFractionalBrownianMotion(SubclassBaseFile):
    ResourceType = 0x2318CE3E
    ParentResourceType = _Operator.ResourceType
    parent: _Operator

