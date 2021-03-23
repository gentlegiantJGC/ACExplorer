from pyUbiForge2.api.game import SubclassBaseFile
from .Operator import Operator as _Operator


class OperatorTerrainMasks(SubclassBaseFile):
    ResourceType = 0xAEE026FD
    ParentResourceType = _Operator.ResourceType
    parent: _Operator

