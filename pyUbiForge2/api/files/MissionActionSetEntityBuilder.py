from pyUbiForge2.api.game import SubclassBaseFile
from .MissionAction import MissionAction as _MissionAction


class MissionActionSetEntityBuilder(SubclassBaseFile):
    ResourceType = 0x2AAB3307
    ParentResourceType = _MissionAction.ResourceType
    parent: _MissionAction

