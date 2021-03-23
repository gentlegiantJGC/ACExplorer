from pyUbiForge2.api.game import SubclassBaseFile
from .CSrvAbstract import CSrvAbstract as _CSrvAbstract


class ICSrvNavigationEngine(SubclassBaseFile):
    ResourceType = 0x47386BBF
    ParentResourceType = _CSrvAbstract.ResourceType
    parent: _CSrvAbstract

