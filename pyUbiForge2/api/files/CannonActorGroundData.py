from pyUbiForge2.api.game import SubclassBaseFile
from .ActorContextData import ActorContextData as _ActorContextData


class CannonActorGroundData(SubclassBaseFile):
    ResourceType = 0x4B330A8F
    ParentResourceType = _ActorContextData.ResourceType
    parent: _ActorContextData
