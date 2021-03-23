from pyUbiForge2.api.game import SubclassBaseFile
from .Operator import Operator as _Operator


class UVTransformOperator(SubclassBaseFile):
    ResourceType = 0xEADF9820
    ParentResourceType = _Operator.ResourceType
    parent: _Operator
