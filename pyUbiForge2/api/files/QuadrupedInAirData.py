from pyUbiForge2.api.game import SubclassBaseFile
from .ActorContextData import ActorContextData as _ActorContextData


class QuadrupedInAirData(SubclassBaseFile):
    ResourceType = 0x7749FB22
    ParentResourceType = _ActorContextData.ResourceType
    parent: _ActorContextData
