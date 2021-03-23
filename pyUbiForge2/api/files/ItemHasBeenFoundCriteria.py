from pyUbiForge2.api.game import SubclassBaseFile
from .ItemCriteria import ItemCriteria as _ItemCriteria


class ItemHasBeenFoundCriteria(SubclassBaseFile):
    ResourceType = 0xF59BDB27
    ParentResourceType = _ItemCriteria.ResourceType
    parent: _ItemCriteria

