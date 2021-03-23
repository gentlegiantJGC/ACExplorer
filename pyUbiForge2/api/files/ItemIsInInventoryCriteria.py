from pyUbiForge2.api.game import SubclassBaseFile
from .ItemCriteria import ItemCriteria as _ItemCriteria


class ItemIsInInventoryCriteria(SubclassBaseFile):
    ResourceType = 0xE7784A9F
    ParentResourceType = _ItemCriteria.ResourceType
    parent: _ItemCriteria
