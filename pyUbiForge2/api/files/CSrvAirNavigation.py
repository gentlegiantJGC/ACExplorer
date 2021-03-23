from pyUbiForge2.api.game import SubclassBaseFile
from .CSrvAbstract import CSrvAbstract as _CSrvAbstract


class CSrvAirNavigation(SubclassBaseFile):
    ResourceType = 0x0C967B89
    ParentResourceType = _CSrvAbstract.ResourceType
    parent: _CSrvAbstract
