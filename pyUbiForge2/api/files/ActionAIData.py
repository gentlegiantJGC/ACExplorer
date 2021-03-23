from pyUbiForge2.api.game import SubclassBaseFile
from .AIAction import AIAction as _AIAction


class ActionAIData(SubclassBaseFile):
    ResourceType = 0x79673ACB
    ParentResourceType = _AIAction.ResourceType
    parent: _AIAction

