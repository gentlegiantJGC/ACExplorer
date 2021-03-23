from pyUbiForge2.api.game import SubclassBaseFile
from .ConstantValue import ConstantValue as _ConstantValue


class ConstantQuaternionValue(SubclassBaseFile):
    ResourceType = 0x9FC95AD5
    ParentResourceType = _ConstantValue.ResourceType
    parent: _ConstantValue
