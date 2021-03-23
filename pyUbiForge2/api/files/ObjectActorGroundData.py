from pyUbiForge2.api.game import SubclassBaseFile
from .ActorContextData import ActorContextData as _ActorContextData


class ObjectActorGroundData(SubclassBaseFile):
    ResourceType = 0x40A2D8E7
    ParentResourceType = _ActorContextData.ResourceType
    parent: _ActorContextData
