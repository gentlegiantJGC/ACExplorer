from pyUbiForge2.api.game import SubclassBaseFile
from .CSAbstract import CSAbstract as _CSAbstract


class CSDanger(SubclassBaseFile):
    ResourceType = 0xD0762DAD
    ParentResourceType = _CSAbstract.ResourceType
    parent: _CSAbstract

