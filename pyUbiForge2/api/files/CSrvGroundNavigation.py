from pyUbiForge2.api.game import SubclassBaseFile
from .CSrvAbstract import CSrvAbstract as _CSrvAbstract


class CSrvGroundNavigation(SubclassBaseFile):
    ResourceType = 0xA3E8C4A5
    ParentResourceType = _CSrvAbstract.ResourceType
    parent: _CSrvAbstract
