from pyUbiForge2.api.game import SubclassBaseFile
from .CSAbstract import CSAbstract as _CSAbstract


class CSDeath(SubclassBaseFile):
    ResourceType = 0x8231C7F4
    ParentResourceType = _CSAbstract.ResourceType
    parent: _CSAbstract
