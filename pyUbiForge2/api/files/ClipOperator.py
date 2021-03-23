from pyUbiForge2.api.game import SubclassBaseFile
from .Operator import Operator as _Operator


class ClipOperator(SubclassBaseFile):
    ResourceType = 0xF0455141
    ParentResourceType = _Operator.ResourceType
    parent: _Operator
