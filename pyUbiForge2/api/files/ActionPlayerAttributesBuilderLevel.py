from pyUbiForge2.api.game import SubclassBaseFile
from .AIAction import AIAction as _AIAction


class ActionPlayerAttributesBuilderLevel(SubclassBaseFile):
    ResourceType = 0xA83C70A9
    ParentResourceType = _AIAction.ResourceType
    parent: _AIAction
