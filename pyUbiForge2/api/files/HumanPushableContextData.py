from pyUbiForge2.api.game import SubclassBaseFile
from .ActorContextData import ActorContextData as _ActorContextData


class HumanPushableContextData(SubclassBaseFile):
    ResourceType = 0x0BF8A26C
    ParentResourceType = _ActorContextData.ResourceType
    parent: _ActorContextData
