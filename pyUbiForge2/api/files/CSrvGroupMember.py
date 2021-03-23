from pyUbiForge2.api.game import SubclassBaseFile
from .CSrvAbstract import CSrvAbstract as _CSrvAbstract


class CSrvGroupMember(SubclassBaseFile):
    ResourceType = 0x06A717F0
    ParentResourceType = _CSrvAbstract.ResourceType
    parent: _CSrvAbstract

