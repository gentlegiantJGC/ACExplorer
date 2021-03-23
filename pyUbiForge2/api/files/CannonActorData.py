from pyUbiForge2.api.game import SubclassBaseFile
from .AIActorData import AIActorData as _AIActorData


class CannonActorData(SubclassBaseFile):
    ResourceType = 0xFD6C8A3C
    ParentResourceType = _AIActorData.ResourceType
    parent: _AIActorData
