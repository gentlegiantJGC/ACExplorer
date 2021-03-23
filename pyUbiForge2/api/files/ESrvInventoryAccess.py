from pyUbiForge2.api.game import SubclassBaseFile
from .CSrvAbstract import CSrvAbstract as _CSrvAbstract


class ESrvInventoryAccess(SubclassBaseFile):
    ResourceType = 0xE32A8929
    ParentResourceType = _CSrvAbstract.ResourceType
    parent: _CSrvAbstract
