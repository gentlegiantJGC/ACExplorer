from pyUbiForge2.api.game import SubclassBaseFile
from .AbstractMissionActionPack import AbstractMissionActionPack as _AbstractMissionActionPack


class MissionGroupActionPack(SubclassBaseFile):
    ResourceType = 0x9B2AEAF3
    ParentResourceType = _AbstractMissionActionPack.ResourceType
    parent: _AbstractMissionActionPack

