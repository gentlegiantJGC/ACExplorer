from pyUbiForge2.api.game import SubclassBaseFile
from .CSrvAbstract import CSrvAbstract as _CSrvAbstract


class CSrvLoot(SubclassBaseFile):
    ResourceType = 0xC731F93D
    ParentResourceType = _CSrvAbstract.ResourceType
    parent: _CSrvAbstract

