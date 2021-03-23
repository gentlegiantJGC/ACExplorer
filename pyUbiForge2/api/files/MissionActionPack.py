from pyUbiForge2.api.game import SubclassBaseFile
from .AbstractMissionActionPack import (
    AbstractMissionActionPack as _AbstractMissionActionPack,
)


class MissionActionPack(SubclassBaseFile):
    ResourceType = 0xD9AA11B9
    ParentResourceType = _AbstractMissionActionPack.ResourceType
    parent: _AbstractMissionActionPack
