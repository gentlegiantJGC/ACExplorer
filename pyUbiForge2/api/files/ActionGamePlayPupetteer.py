from pyUbiForge2.api.game import SubclassBaseFile
from .AIAction import AIAction as _AIAction


class ActionGamePlayPupetteer(SubclassBaseFile):
    ResourceType = 0x6D8F3BB5
    ParentResourceType = _AIAction.ResourceType
    parent: _AIAction

