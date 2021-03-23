from pyUbiForge2.api.game import SubclassBaseFile
from .ActorContextData import ActorContextData as _ActorContextData


class GliderActorInAirData(SubclassBaseFile):
    ResourceType = 0x0ED8B620
    ParentResourceType = _ActorContextData.ResourceType
    parent: _ActorContextData
