from pyUbiForge2.api.game import SubclassBaseFile
from .ActorContextData import ActorContextData as _ActorContextData


class HumanHayStackData(SubclassBaseFile):
    ResourceType = 0x5C389244
    ParentResourceType = _ActorContextData.ResourceType
    parent: _ActorContextData

