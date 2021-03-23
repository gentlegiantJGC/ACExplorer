from pyUbiForge2.api.game import SubclassBaseFile
from .AIAction import AIAction as _AIAction


class ActionFightRematchingDelay(SubclassBaseFile):
    ResourceType = 0xA1C5EF94
    ParentResourceType = _AIAction.ResourceType
    parent: _AIAction

