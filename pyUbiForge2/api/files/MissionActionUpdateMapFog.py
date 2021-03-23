from pyUbiForge2.api.game import SubclassBaseFile
from .MissionAction import MissionAction as _MissionAction


class MissionActionUpdateMapFog(SubclassBaseFile):
    ResourceType = 0x19E23ED9
    ParentResourceType = _MissionAction.ResourceType
    parent: _MissionAction

