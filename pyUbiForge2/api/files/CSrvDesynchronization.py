from pyUbiForge2.api.game import SubclassBaseFile
from .CSrvAbstract import CSrvAbstract as _CSrvAbstract


class CSrvDesynchronization(SubclassBaseFile):
    ResourceType = 0x4F741E1D
    ParentResourceType = _CSrvAbstract.ResourceType
    parent: _CSrvAbstract
