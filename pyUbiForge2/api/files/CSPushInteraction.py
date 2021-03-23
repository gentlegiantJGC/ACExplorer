from pyUbiForge2.api.game import SubclassBaseFile
from .CSAbstract import CSAbstract as _CSAbstract


class CSPushInteraction(SubclassBaseFile):
    ResourceType = 0x35014361
    ParentResourceType = _CSAbstract.ResourceType
    parent: _CSAbstract
