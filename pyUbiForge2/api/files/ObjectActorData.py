from pyUbiForge2.api.game import SubclassBaseFile
from .AIActorData import AIActorData as _AIActorData


class ObjectActorData(SubclassBaseFile):
    ResourceType = 0x4F454B7D
    ParentResourceType = _AIActorData.ResourceType
    parent: _AIActorData
