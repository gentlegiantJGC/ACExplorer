from pyUbiForge2.api.game import SubclassBaseFile
from .AIAction import AIAction as _AIAction


class AddDefaultWorldTransitionPortalAction(SubclassBaseFile):
    ResourceType = 0x354A551D
    ParentResourceType = _AIAction.ResourceType
    parent: _AIAction

