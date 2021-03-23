from pyUbiForge2.api.game import SubclassBaseFile
from .Operator import Operator as _Operator


class LightingStack(SubclassBaseFile):
    ResourceType = 0xCCBF7D14
    ParentResourceType = _Operator.ResourceType
    parent: _Operator
