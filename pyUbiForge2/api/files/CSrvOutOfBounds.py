from pyUbiForge2.api.game import SubclassBaseFile
from .CSrvAbstract import CSrvAbstract as _CSrvAbstract


class CSrvOutOfBounds(SubclassBaseFile):
    ResourceType = 0x2963FA96
    ParentResourceType = _CSrvAbstract.ResourceType
    parent: _CSrvAbstract

