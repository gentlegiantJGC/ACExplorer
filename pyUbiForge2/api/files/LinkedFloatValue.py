from pyUbiForge2.api.game import SubclassBaseFile
from .LinkedValue import LinkedValue as _LinkedValue


class LinkedFloatValue(SubclassBaseFile):
    ResourceType = 0x28F542F6
    ParentResourceType = _LinkedValue.ResourceType
    parent: _LinkedValue
