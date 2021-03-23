from pyUbiForge2.api.game import SubclassBaseFile
from .DefaultValue import DefaultValue as _DefaultValue


class DefaultQuaternionValue(SubclassBaseFile):
    ResourceType = 0x7794AB39
    ParentResourceType = _DefaultValue.ResourceType
    parent: _DefaultValue

