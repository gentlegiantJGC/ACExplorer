from pyUbiForge2.api.game import SubclassBaseFile
from .AIActorData import AIActorData as _AIActorData


class HumanData(SubclassBaseFile):
    ResourceType = 0x51E9F95F
    ParentResourceType = _AIActorData.ResourceType
    parent: _AIActorData
