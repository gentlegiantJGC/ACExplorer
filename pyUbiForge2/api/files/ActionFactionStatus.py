from pyUbiForge2.api.game import SubclassBaseFile
from .AIAction import AIAction as _AIAction


class ActionFactionStatus(SubclassBaseFile):
    ResourceType = 0x983E4E0C
    ParentResourceType = _AIAction.ResourceType
    parent: _AIAction
