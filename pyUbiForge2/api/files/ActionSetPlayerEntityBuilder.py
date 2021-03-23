from pyUbiForge2.api.game import SubclassBaseFile
from .AIAction import AIAction as _AIAction


class ActionSetPlayerEntityBuilder(SubclassBaseFile):
    ResourceType = 0x5D7968E7
    ParentResourceType = _AIAction.ResourceType
    parent: _AIAction
