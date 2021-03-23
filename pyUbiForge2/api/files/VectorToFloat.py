from pyUbiForge2.api.game import SubclassBaseFile
from .Operator import Operator as _Operator


class VectorToFloat(SubclassBaseFile):
    ResourceType = 0xADAF4ED2
    ParentResourceType = _Operator.ResourceType
    parent: _Operator
