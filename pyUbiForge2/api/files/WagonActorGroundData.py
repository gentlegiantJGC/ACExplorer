from pyUbiForge2.api.game import SubclassBaseFile
from .ActorContextData import ActorContextData as _ActorContextData


class WagonActorGroundData(SubclassBaseFile):
    ResourceType = 0x4F987343
    ParentResourceType = _ActorContextData.ResourceType
    parent: _ActorContextData

