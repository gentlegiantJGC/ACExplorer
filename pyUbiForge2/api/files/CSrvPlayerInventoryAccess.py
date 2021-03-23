from pyUbiForge2.api.game import SubclassBaseFile
from .CSrvAbstract import CSrvAbstract as _CSrvAbstract


class CSrvPlayerInventoryAccess(SubclassBaseFile):
    ResourceType = 0x0D729318
    ParentResourceType = _CSrvAbstract.ResourceType
    parent: _CSrvAbstract
