from pyUbiForge2.api.game import SubclassBaseFile
from .MissionAction import MissionAction as _MissionAction


class MissionActionAddDefaultWorldTransitionPortalAction(SubclassBaseFile):
    ResourceType = 0x0B7078D5
    ParentResourceType = _MissionAction.ResourceType
    parent: _MissionAction
