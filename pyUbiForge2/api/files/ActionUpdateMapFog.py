from pyUbiForge2.api.game import SubclassBaseFile
from .AIAction import AIAction as _AIAction


class ActionUpdateMapFog(SubclassBaseFile):
    ResourceType = 0x0289627D
    ParentResourceType = _AIAction.ResourceType
    parent: _AIAction

