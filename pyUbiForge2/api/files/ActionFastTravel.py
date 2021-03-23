from pyUbiForge2.api.game import SubclassBaseFile
from .AIAction import AIAction as _AIAction


class ActionFastTravel(SubclassBaseFile):
    ResourceType = 0x640EEE1B
    ParentResourceType = _AIAction.ResourceType
    parent: _AIAction

