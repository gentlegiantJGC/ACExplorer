from pyUbiForge2.api.game import SubclassBaseFile
from .ActorContextData import ActorContextData as _ActorContextData


class HumanCannonOperatorData(SubclassBaseFile):
    ResourceType = 0x9291AEF1
    ParentResourceType = _ActorContextData.ResourceType
    parent: _ActorContextData
