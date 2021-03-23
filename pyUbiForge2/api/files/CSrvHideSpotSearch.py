from pyUbiForge2.api.game import SubclassBaseFile
from .CSrvAbstract import CSrvAbstract as _CSrvAbstract


class CSrvHideSpotSearch(SubclassBaseFile):
    ResourceType = 0x125ECE99
    ParentResourceType = _CSrvAbstract.ResourceType
    parent: _CSrvAbstract
