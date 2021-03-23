from pyUbiForge2.api.game import SubclassBaseFile
from .AIActorData import AIActorData as _AIActorData


class QuadrupedData(SubclassBaseFile):
    ResourceType = 0xE054DBC9
    ParentResourceType = _AIActorData.ResourceType
    parent: _AIActorData

