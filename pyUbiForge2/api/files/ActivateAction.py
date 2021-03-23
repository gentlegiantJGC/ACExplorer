from pyUbiForge2.api.game import SubclassBaseFile
from .AIAction import AIAction as _AIAction


class ActivateAction(SubclassBaseFile):
    ResourceType = 0x02987FF1
    ParentResourceType = _AIAction.ResourceType
    parent: _AIAction
