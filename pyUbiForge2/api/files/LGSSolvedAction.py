from pyUbiForge2.api.game import SubclassBaseFile
from .AIAction import AIAction as _AIAction


class LGSSolvedAction(SubclassBaseFile):
    ResourceType = 0x1E128D7D
    ParentResourceType = _AIAction.ResourceType
    parent: _AIAction

