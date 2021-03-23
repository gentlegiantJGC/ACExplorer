from pyUbiForge2.api.game import SubclassBaseFile
from .ItemCriteria import ItemCriteria as _ItemCriteria


class CodexPageIsInInventoryCriteria(SubclassBaseFile):
    ResourceType = 0x44D62E75
    ParentResourceType = _ItemCriteria.ResourceType
    parent: _ItemCriteria

