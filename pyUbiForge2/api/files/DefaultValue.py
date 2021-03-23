from pyUbiForge2.api.game import SubclassBaseFile
from .Operator import Operator as _Operator


class DefaultValue(SubclassBaseFile):
    ResourceType = 0xDC53E7D5
    ParentResourceType = _Operator.ResourceType
    parent: _Operator

