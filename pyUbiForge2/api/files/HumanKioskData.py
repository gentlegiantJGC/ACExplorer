from pyUbiForge2.api.game import SubclassBaseFile
from .ActorContextData import ActorContextData as _ActorContextData


class HumanKioskData(SubclassBaseFile):
    ResourceType = 0x71627BDB
    ParentResourceType = _ActorContextData.ResourceType
    parent: _ActorContextData
