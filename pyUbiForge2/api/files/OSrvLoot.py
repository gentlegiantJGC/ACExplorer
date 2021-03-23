from pyUbiForge2.api.game import SubclassBaseFile
from .OSrvAbstract import OSrvAbstract as _OSrvAbstract


class OSrvLoot(SubclassBaseFile):
    ResourceType = 0x909EEC72
    ParentResourceType = _OSrvAbstract.ResourceType
    parent: _OSrvAbstract
