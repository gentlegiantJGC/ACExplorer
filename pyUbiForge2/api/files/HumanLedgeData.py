from pyUbiForge2.api.game import SubclassBaseFile
from .ActorContextData import ActorContextData as _ActorContextData


class HumanLedgeData(SubclassBaseFile):
    ResourceType = 0x68FE5487
    ParentResourceType = _ActorContextData.ResourceType
    parent: _ActorContextData

