from pyUbiForge2.api.game import SubclassBaseFile
from .CSrvAbstract import CSrvAbstract as _CSrvAbstract


class CSrvWitnessPropagation(SubclassBaseFile):
    ResourceType = 0x32191DBC
    ParentResourceType = _CSrvAbstract.ResourceType
    parent: _CSrvAbstract
