from pyUbiForge2.api.game import SubclassBaseFile
from .AIAction import AIAction as _AIAction


class ActionHorse(SubclassBaseFile):
    ResourceType = 0x0E0344DE
    ParentResourceType = _AIAction.ResourceType
    parent: _AIAction

