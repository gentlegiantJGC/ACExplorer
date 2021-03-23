from pyUbiForge2.api.game import SubclassBaseFile
from .ActorContextData import ActorContextData as _ActorContextData


class HumanWallingData(SubclassBaseFile):
    ResourceType = 0xD79FB15B
    ParentResourceType = _ActorContextData.ResourceType
    parent: _ActorContextData

