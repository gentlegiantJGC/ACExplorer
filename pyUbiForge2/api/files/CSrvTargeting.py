from pyUbiForge2.api.game import SubclassBaseFile
from .CSrvAbstract import CSrvAbstract as _CSrvAbstract


class CSrvTargeting(SubclassBaseFile):
    ResourceType = 0x9E17EEC2
    ParentResourceType = _CSrvAbstract.ResourceType
    parent: _CSrvAbstract

