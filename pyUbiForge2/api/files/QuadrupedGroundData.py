from pyUbiForge2.api.game import SubclassBaseFile
from .ActorContextData import ActorContextData as _ActorContextData


class QuadrupedGroundData(SubclassBaseFile):
    ResourceType = 0x2A7E8433
    ParentResourceType = _ActorContextData.ResourceType
    parent: _ActorContextData

