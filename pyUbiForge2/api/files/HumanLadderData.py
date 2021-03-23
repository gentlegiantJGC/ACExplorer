from pyUbiForge2.api.game import SubclassBaseFile
from .ActorContextData import ActorContextData as _ActorContextData


class HumanLadderData(SubclassBaseFile):
    ResourceType = 0x3E5C9DDB
    ParentResourceType = _ActorContextData.ResourceType
    parent: _ActorContextData

