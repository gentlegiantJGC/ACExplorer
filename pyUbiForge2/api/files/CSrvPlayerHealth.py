from pyUbiForge2.api.game import SubclassBaseFile
from .CSrvAbstract import CSrvAbstract as _CSrvAbstract


class CSrvPlayerHealth(SubclassBaseFile):
    ResourceType = 0xFA21FFCF
    ParentResourceType = _CSrvAbstract.ResourceType
    parent: _CSrvAbstract
