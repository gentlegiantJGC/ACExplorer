from pyUbiForge2.api.game import SubclassBaseFile
from .CSrvAbstract import CSrvAbstract as _CSrvAbstract


class CSrvNPCHealth(SubclassBaseFile):
    ResourceType = 0x57EEEEC7
    ParentResourceType = _CSrvAbstract.ResourceType
    parent: _CSrvAbstract

