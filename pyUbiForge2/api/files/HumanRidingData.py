from pyUbiForge2.api.game import SubclassBaseFile
from .ActorContextData import ActorContextData as _ActorContextData


class HumanRidingData(SubclassBaseFile):
    ResourceType = 0xF8750A14
    ParentResourceType = _ActorContextData.ResourceType
    parent: _ActorContextData

