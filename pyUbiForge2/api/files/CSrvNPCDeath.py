from pyUbiForge2.api.game import SubclassBaseFile
from .CSrvAbstract import CSrvAbstract as _CSrvAbstract


class CSrvNPCDeath(SubclassBaseFile):
    ResourceType = 0xDADBBB2D
    ParentResourceType = _CSrvAbstract.ResourceType
    parent: _CSrvAbstract
