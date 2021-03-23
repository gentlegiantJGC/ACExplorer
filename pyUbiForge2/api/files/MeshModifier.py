from pyUbiForge2.api.game import SubclassBaseFile
from .Operator import Operator as _Operator


class MeshModifier(SubclassBaseFile):
    ResourceType = 0x39B433EE
    ParentResourceType = _Operator.ResourceType
    parent: _Operator

