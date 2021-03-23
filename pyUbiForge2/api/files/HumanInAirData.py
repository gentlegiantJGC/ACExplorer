from pyUbiForge2.api.game import SubclassBaseFile
from .ActorContextData import ActorContextData as _ActorContextData


class HumanInAirData(SubclassBaseFile):
    ResourceType = 0x9EDC74AC
    ParentResourceType = _ActorContextData.ResourceType
    parent: _ActorContextData

