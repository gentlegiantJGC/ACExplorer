from pyUbiForge2.api.game import SubclassBaseFile
from .CSrvAbstract import CSrvAbstract as _CSrvAbstract


class CSrvPickpocketBump(SubclassBaseFile):
    ResourceType = 0xC5F51B5E
    ParentResourceType = _CSrvAbstract.ResourceType
    parent: _CSrvAbstract

