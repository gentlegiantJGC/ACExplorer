from pyUbiForge2.api.game import SubclassBaseFile
from .AIAction import AIAction as _AIAction


class ActionDLCAlternateIcon(SubclassBaseFile):
    ResourceType = 0x1574A5B9
    ParentResourceType = _AIAction.ResourceType
    parent: _AIAction

