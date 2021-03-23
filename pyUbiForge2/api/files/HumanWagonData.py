from pyUbiForge2.api.game import SubclassBaseFile
from .ActorContextData import ActorContextData as _ActorContextData


class HumanWagonData(SubclassBaseFile):
    ResourceType = 0x5B4F4659
    ParentResourceType = _ActorContextData.ResourceType
    parent: _ActorContextData
