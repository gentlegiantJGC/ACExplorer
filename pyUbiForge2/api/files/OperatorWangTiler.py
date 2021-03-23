from pyUbiForge2.api.game import SubclassBaseFile
from .Operator import Operator as _Operator


class OperatorWangTiler(SubclassBaseFile):
    ResourceType = 0x9AB7FEFA
    ParentResourceType = _Operator.ResourceType
    parent: _Operator
