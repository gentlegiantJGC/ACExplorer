from pyUbiForge2.api.game import SubclassBaseFile
from .AIAction import AIAction as _AIAction


class MiniMapAction(SubclassBaseFile):
    ResourceType = 0x4128CF13
    ParentResourceType = _AIAction.ResourceType
    parent: _AIAction

