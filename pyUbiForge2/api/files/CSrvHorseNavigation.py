from pyUbiForge2.api.game import SubclassBaseFile
from .CSrvAbstract import CSrvAbstract as _CSrvAbstract


class CSrvHorseNavigation(SubclassBaseFile):
    ResourceType = 0xE4A854B0
    ParentResourceType = _CSrvAbstract.ResourceType
    parent: _CSrvAbstract

