from pyUbiForge2.api.game import SubclassBaseFile
from .NPCBehaviorData import NPCBehaviorData as _NPCBehaviorData


class NPCAssassinGameData(SubclassBaseFile):
    ResourceType = 0x9DC61220
    ParentResourceType = _NPCBehaviorData.ResourceType
    parent: _NPCBehaviorData

