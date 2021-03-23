from pyUbiForge2.api.game import SubclassBaseFile
from .ActorContextData import ActorContextData as _ActorContextData


class GliderActorGroundData(SubclassBaseFile):
    ResourceType = 0xC4097452
    ParentResourceType = _ActorContextData.ResourceType
    parent: _ActorContextData

