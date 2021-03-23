from pyUbiForge2.api.game import SubclassBaseFile
from .DefaultValue import DefaultValue as _DefaultValue


class DefaultVectorValue(SubclassBaseFile):
    ResourceType = 0xD6184774
    ParentResourceType = _DefaultValue.ResourceType
    parent: _DefaultValue
