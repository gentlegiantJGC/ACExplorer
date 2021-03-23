from pyUbiForge2.api.game import SubclassBaseFile
from .NPCBehaviorData import NPCBehaviorData as _NPCBehaviorData


class BhvHorseData(SubclassBaseFile):
    ResourceType = 0xABE9D122
    ParentResourceType = _NPCBehaviorData.ResourceType
    parent: _NPCBehaviorData
