from pyUbiForge2.api.game import SubclassBaseFile
from .ActorContextData import ActorContextData as _ActorContextData


class HumanDeadData(SubclassBaseFile):
    ResourceType = 0x8A9BEA05
    ParentResourceType = _ActorContextData.ResourceType
    parent: _ActorContextData
