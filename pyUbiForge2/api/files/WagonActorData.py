from pyUbiForge2.api.game import SubclassBaseFile
from .AIActorData import AIActorData as _AIActorData


class WagonActorData(SubclassBaseFile):
    ResourceType = 0xC94F01BE
    ParentResourceType = _AIActorData.ResourceType
    parent: _AIActorData

