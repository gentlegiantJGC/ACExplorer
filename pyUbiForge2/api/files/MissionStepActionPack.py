from pyUbiForge2.api.game import SubclassBaseFile
from .AbstractMissionActionPack import (
    AbstractMissionActionPack as _AbstractMissionActionPack,
)


class MissionStepActionPack(SubclassBaseFile):
    ResourceType = 0xBC11BD33
    ParentResourceType = _AbstractMissionActionPack.ResourceType
    parent: _AbstractMissionActionPack
