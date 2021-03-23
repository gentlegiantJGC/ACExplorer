from pyUbiForge2.api.game import SubclassBaseFile
from .CSAbstract import CSAbstract as _CSAbstract


class CSDamage(SubclassBaseFile):
    ResourceType = 0x77AB19B4
    ParentResourceType = _CSAbstract.ResourceType
    parent: _CSAbstract
