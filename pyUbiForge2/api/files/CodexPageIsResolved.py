from pyUbiForge2.api.game import SubclassBaseFile
from .ItemCriteria import ItemCriteria as _ItemCriteria


class CodexPageIsResolved(SubclassBaseFile):
    ResourceType = 0xA6E4339C
    ParentResourceType = _ItemCriteria.ResourceType
    parent: _ItemCriteria
