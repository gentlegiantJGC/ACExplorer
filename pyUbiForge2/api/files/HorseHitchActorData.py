from pyUbiForge2.api.game import SubclassBaseFile
from .AIActorData import AIActorData as _AIActorData


class HorseHitchActorData(SubclassBaseFile):
    ResourceType = 0xB6D908CF
    ParentResourceType = _AIActorData.ResourceType
    parent: _AIActorData

