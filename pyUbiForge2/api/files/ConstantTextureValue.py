from pyUbiForge2.api.game import SubclassBaseFile
from .ConstantValue import ConstantValue as _ConstantValue


class ConstantTextureValue(SubclassBaseFile):
    ResourceType = 0x3203D42D
    ParentResourceType = _ConstantValue.ResourceType
    parent: _ConstantValue
