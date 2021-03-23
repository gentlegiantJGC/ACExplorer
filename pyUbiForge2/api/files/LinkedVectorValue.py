from pyUbiForge2.api.game import SubclassBaseFile
from .LinkedValue import LinkedValue as _LinkedValue


class LinkedVectorValue(SubclassBaseFile):
    ResourceType = 0x7A1A429A
    ParentResourceType = _LinkedValue.ResourceType
    parent: _LinkedValue
