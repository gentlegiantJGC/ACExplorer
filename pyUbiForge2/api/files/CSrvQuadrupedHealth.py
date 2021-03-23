from pyUbiForge2.api.game import SubclassBaseFile
from .CSrvAbstract import CSrvAbstract as _CSrvAbstract


class CSrvQuadrupedHealth(SubclassBaseFile):
    ResourceType = 0x0ED54777
    ParentResourceType = _CSrvAbstract.ResourceType
    parent: _CSrvAbstract
