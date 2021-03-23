from pyUbiForge2.api.game import SubclassBaseFile
from .LinkedValue import LinkedValue as _LinkedValue


class LinkedQuaternionValue(SubclassBaseFile):
    ResourceType = 0xAAA9D298
    ParentResourceType = _LinkedValue.ResourceType
    parent: _LinkedValue

