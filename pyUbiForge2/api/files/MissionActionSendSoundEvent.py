from pyUbiForge2.api.game import SubclassBaseFile
from .MissionAction import MissionAction as _MissionAction


class MissionActionSendSoundEvent(SubclassBaseFile):
    ResourceType = 0xDF63DD80
    ParentResourceType = _MissionAction.ResourceType
    parent: _MissionAction

