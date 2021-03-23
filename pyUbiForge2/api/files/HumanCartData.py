from pyUbiForge2.api.game import SubclassBaseFile
from .ActorContextData import ActorContextData as _ActorContextData


class HumanCartData(SubclassBaseFile):
    ResourceType = 0x8939F73C
    ParentResourceType = _ActorContextData.ResourceType
    parent: _ActorContextData

