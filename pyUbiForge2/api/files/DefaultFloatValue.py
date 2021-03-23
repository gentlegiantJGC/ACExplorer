from pyUbiForge2.api.game import SubclassBaseFile
from .DefaultValue import DefaultValue as _DefaultValue


class DefaultFloatValue(SubclassBaseFile):
    ResourceType = 0x9609ECDD
    ParentResourceType = _DefaultValue.ResourceType
    parent: _DefaultValue
