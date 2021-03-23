from pyUbiForge2.api.game import SubclassBaseFile
from .CSAbstract import CSAbstract as _CSAbstract


class CSProximity(SubclassBaseFile):
    ResourceType = 0x08442855
    ParentResourceType = _CSAbstract.ResourceType
    parent: _CSAbstract
