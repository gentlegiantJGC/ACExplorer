from pyUbiForge2.api.game import SubclassBaseFile
from .AIAction import AIAction as _AIAction


class ActionTransfertIncomeToTheBank(SubclassBaseFile):
    ResourceType = 0xEC446F0D
    ParentResourceType = _AIAction.ResourceType
    parent: _AIAction
