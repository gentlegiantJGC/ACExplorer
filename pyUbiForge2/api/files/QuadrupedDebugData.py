from pyUbiForge2.api.game import SubclassBaseFile
from .ActorContextData import ActorContextData as _ActorContextData


class QuadrupedDebugData(SubclassBaseFile):
    ResourceType = 0xF92DF930
    ParentResourceType = _ActorContextData.ResourceType
    parent: _ActorContextData
