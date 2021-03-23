from pyUbiForge2.api.game import SubclassBaseFile
from .CSAbstract import CSAbstract as _CSAbstract


class CSPlayerLineOfSight(SubclassBaseFile):
    ResourceType = 0xE576690B
    ParentResourceType = _CSAbstract.ResourceType
    parent: _CSAbstract
