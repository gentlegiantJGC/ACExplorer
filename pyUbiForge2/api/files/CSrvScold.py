from pyUbiForge2.api.game import SubclassBaseFile
from .CSrvAbstract import CSrvAbstract as _CSrvAbstract


class CSrvScold(SubclassBaseFile):
    ResourceType = 0xEA0F1096
    ParentResourceType = _CSrvAbstract.ResourceType
    parent: _CSrvAbstract

