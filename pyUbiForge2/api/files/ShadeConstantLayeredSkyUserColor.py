from pyUbiForge2.api.game import SubclassBaseFile
from .Operator import Operator as _Operator


class ShadeConstantLayeredSkyUserColor(SubclassBaseFile):
    ResourceType = 0xF202BE1E
    ParentResourceType = _Operator.ResourceType
    parent: _Operator
