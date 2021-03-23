from pyUbiForge2.api.game import SubclassBaseFile
from .ActorContextData import ActorContextData as _ActorContextData


class HumanCustomActionData(SubclassBaseFile):
    ResourceType = 0x13AEF6C5
    ParentResourceType = _ActorContextData.ResourceType
    parent: _ActorContextData

