from pyUbiForge2.api.game import SubclassBaseFile
from .CSrvAbstract import CSrvAbstract as _CSrvAbstract


class CSrvLadderNavigation(SubclassBaseFile):
    ResourceType = 0xBD54F41A
    ParentResourceType = _CSrvAbstract.ResourceType
    parent: _CSrvAbstract
