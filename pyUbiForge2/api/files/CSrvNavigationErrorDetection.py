from pyUbiForge2.api.game import SubclassBaseFile
from .CSrvAbstract import CSrvAbstract as _CSrvAbstract


class CSrvNavigationErrorDetection(SubclassBaseFile):
    ResourceType = 0xC6E91FB2
    ParentResourceType = _CSrvAbstract.ResourceType
    parent: _CSrvAbstract

