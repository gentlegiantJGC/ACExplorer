from pyUbiForge2.api.game import SubclassBaseFile
from .DefaultValue import DefaultValue as _DefaultValue


class DefaultIntegerValue(SubclassBaseFile):
    ResourceType = 0xCEFF2662
    ParentResourceType = _DefaultValue.ResourceType
    parent: _DefaultValue

