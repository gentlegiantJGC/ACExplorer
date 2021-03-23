from pyUbiForge2.api.game import SubclassBaseFile
from .CSrvAbstract import CSrvAbstract as _CSrvAbstract


class CSrvAssassinAbilities(SubclassBaseFile):
    ResourceType = 0x39227025
    ParentResourceType = _CSrvAbstract.ResourceType
    parent: _CSrvAbstract

