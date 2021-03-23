from pyUbiForge2.api.game import SubclassBaseFile
from .BuildTable import BuildTable as _BuildTable


class EntityBuilder(SubclassBaseFile):
    ResourceType = 0x971A842E
    ParentResourceType = _BuildTable.ResourceType
    parent: _BuildTable

