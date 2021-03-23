from pyUbiForge2.api.game import SubclassBaseFile
from .ItemCriteria import ItemCriteria as _ItemCriteria


class ItemIsInVilla(SubclassBaseFile):
    ResourceType = 0xE7746A9C
    ParentResourceType = _ItemCriteria.ResourceType
    parent: _ItemCriteria
