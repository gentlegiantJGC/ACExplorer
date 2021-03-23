from pyUbiForge2.api.game import SubclassBaseFile
from .CSAbstract import CSAbstract as _CSAbstract


class CSCollision(SubclassBaseFile):
    ResourceType = 0x493B46FA
    ParentResourceType = _CSAbstract.ResourceType
    parent: _CSAbstract

