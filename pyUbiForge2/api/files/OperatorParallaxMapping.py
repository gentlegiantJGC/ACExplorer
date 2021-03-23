from pyUbiForge2.api.game import SubclassBaseFile
from .Operator import Operator as _Operator


class OperatorParallaxMapping(SubclassBaseFile):
    ResourceType = 0xDADE22E4
    ParentResourceType = _Operator.ResourceType
    parent: _Operator

