from pyUbiForge2.api.game import SubclassBaseFile
from .ActorContextData import ActorContextData as _ActorContextData


class DebugContextData(SubclassBaseFile):
    ResourceType = 0xC9D9191E
    ParentResourceType = _ActorContextData.ResourceType
    parent: _ActorContextData
