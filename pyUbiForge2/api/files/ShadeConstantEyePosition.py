from pyUbiForge2.api.game import SubclassBaseFile
from .Operator import Operator as _Operator


class ShadeConstantEyePosition(SubclassBaseFile):
    ResourceType = 0x91B8BCBB
    ParentResourceType = _Operator.ResourceType
    parent: _Operator

