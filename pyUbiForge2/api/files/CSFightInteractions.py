from pyUbiForge2.api.game import SubclassBaseFile
from .CSAbstract import CSAbstract as _CSAbstract


class CSFightInteractions(SubclassBaseFile):
    ResourceType = 0x782FA78F
    ParentResourceType = _CSAbstract.ResourceType
    parent: _CSAbstract
