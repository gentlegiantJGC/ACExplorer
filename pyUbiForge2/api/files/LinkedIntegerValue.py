from pyUbiForge2.api.game import SubclassBaseFile
from .LinkedValue import LinkedValue as _LinkedValue


class LinkedIntegerValue(SubclassBaseFile):
    ResourceType = 0x89E1EB18
    ParentResourceType = _LinkedValue.ResourceType
    parent: _LinkedValue
