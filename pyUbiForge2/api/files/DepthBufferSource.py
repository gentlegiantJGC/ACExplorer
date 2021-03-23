from pyUbiForge2.api.game import SubclassBaseFile
from .Operator import Operator as _Operator


class DepthBufferSource(SubclassBaseFile):
    ResourceType = 0xAF63E32A
    ParentResourceType = _Operator.ResourceType
    parent: _Operator
