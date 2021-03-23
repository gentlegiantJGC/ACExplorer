from pyUbiForge2.api.game import SubclassBaseFile
from .ActorContextData import ActorContextData as _ActorContextData


class HumanSwimData(SubclassBaseFile):
    ResourceType = 0xF56D6848
    ParentResourceType = _ActorContextData.ResourceType
    parent: _ActorContextData

