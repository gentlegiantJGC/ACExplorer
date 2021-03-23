from pyUbiForge2.api.game import SubclassBaseFile
from .Operator import Operator as _Operator


class ReflectionSource(SubclassBaseFile):
    ResourceType = 0x7FAE5D75
    ParentResourceType = _Operator.ResourceType
    parent: _Operator

