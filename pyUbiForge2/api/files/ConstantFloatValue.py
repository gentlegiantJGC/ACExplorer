from pyUbiForge2.api.game import SubclassBaseFile
from .ConstantValue import ConstantValue as _ConstantValue


class ConstantFloatValue(SubclassBaseFile):
    ResourceType = 0xA4755364
    ParentResourceType = _ConstantValue.ResourceType
    parent: _ConstantValue

