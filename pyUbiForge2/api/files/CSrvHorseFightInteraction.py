from pyUbiForge2.api.game import SubclassBaseFile
from .CSrvAbstract import CSrvAbstract as _CSrvAbstract


class CSrvHorseFightInteraction(SubclassBaseFile):
    ResourceType = 0x3774E7C6
    ParentResourceType = _CSrvAbstract.ResourceType
    parent: _CSrvAbstract
