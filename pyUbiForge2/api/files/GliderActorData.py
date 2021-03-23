from pyUbiForge2.api.game import SubclassBaseFile
from .AIActorData import AIActorData as _AIActorData


class GliderActorData(SubclassBaseFile):
    ResourceType = 0x889348DF
    ParentResourceType = _AIActorData.ResourceType
    parent: _AIActorData
