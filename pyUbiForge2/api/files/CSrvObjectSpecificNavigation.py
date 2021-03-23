from pyUbiForge2.api.game import SubclassBaseFile
from .CSrvAbstract import CSrvAbstract as _CSrvAbstract


class CSrvObjectSpecificNavigation(SubclassBaseFile):
    ResourceType = 0x7603E962
    ParentResourceType = _CSrvAbstract.ResourceType
    parent: _CSrvAbstract

