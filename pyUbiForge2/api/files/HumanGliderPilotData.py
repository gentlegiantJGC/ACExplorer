from pyUbiForge2.api.game import SubclassBaseFile
from .ActorContextData import ActorContextData as _ActorContextData


class HumanGliderPilotData(SubclassBaseFile):
    ResourceType = 0xB61807B4
    ParentResourceType = _ActorContextData.ResourceType
    parent: _ActorContextData

