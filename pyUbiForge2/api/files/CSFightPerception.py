from pyUbiForge2.api.game import SubclassBaseFile
from .CSAbstract import CSAbstract as _CSAbstract


class CSFightPerception(SubclassBaseFile):
    ResourceType = 0x4E198B7F
    ParentResourceType = _CSAbstract.ResourceType
    parent: _CSAbstract

