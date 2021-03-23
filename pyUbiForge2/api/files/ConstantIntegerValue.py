from pyUbiForge2.api.game import SubclassBaseFile
from .ConstantValue import ConstantValue as _ConstantValue


class ConstantIntegerValue(SubclassBaseFile):
    ResourceType = 0xA026AFF2
    ParentResourceType = _ConstantValue.ResourceType
    parent: _ConstantValue

