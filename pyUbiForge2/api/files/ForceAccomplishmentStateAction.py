from pyUbiForge2.api.game import SubclassBaseFile
from .AIAction import AIAction as _AIAction


class ForceAccomplishmentStateAction(SubclassBaseFile):
    ResourceType = 0xA9FFB279
    ParentResourceType = _AIAction.ResourceType
    parent: _AIAction

