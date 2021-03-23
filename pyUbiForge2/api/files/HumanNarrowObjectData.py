from pyUbiForge2.api.game import SubclassBaseFile
from .ActorContextData import ActorContextData as _ActorContextData


class HumanNarrowObjectData(SubclassBaseFile):
    ResourceType = 0xE57B9A5D
    ParentResourceType = _ActorContextData.ResourceType
    parent: _ActorContextData

