from pyUbiForge2.api.game import SubclassBaseFile
from .ConstantValue import ConstantValue as _ConstantValue


class ConstantVectorValue(SubclassBaseFile):
    ResourceType = 0x649730E3
    ParentResourceType = _ConstantValue.ResourceType
    parent: _ConstantValue

