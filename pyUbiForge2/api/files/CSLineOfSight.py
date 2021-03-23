from pyUbiForge2.api.game import SubclassBaseFile
from .CSAbstract import CSAbstract as _CSAbstract


class CSLineOfSight(SubclassBaseFile):
    ResourceType = 0x5B7B0E0A
    ParentResourceType = _CSAbstract.ResourceType
    parent: _CSAbstract
