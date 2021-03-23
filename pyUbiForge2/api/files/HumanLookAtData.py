from pyUbiForge2.api.game import SubclassBaseFile
from .ActorContextData import ActorContextData as _ActorContextData


class HumanLookAtData(SubclassBaseFile):
    ResourceType = 0x559FDB6D
    ParentResourceType = _ActorContextData.ResourceType
    parent: _ActorContextData

