from pyUbiForge2.api.game import SubclassBaseFile
from .CSAbstract import CSAbstract as _CSAbstract


class CSVisual(SubclassBaseFile):
    ResourceType = 0x8DAAC5C7
    ParentResourceType = _CSAbstract.ResourceType
    parent: _CSAbstract

