from pyUbiForge2.api.game import SubclassBaseFile
from .Operator import Operator as _Operator


class FXBoneSource(SubclassBaseFile):
    ResourceType = 0x8A687BDB
    ParentResourceType = _Operator.ResourceType
    parent: _Operator

