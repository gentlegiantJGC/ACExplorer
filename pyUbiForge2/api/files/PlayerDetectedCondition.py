from pyUbiForge2.api.game import SubclassBaseFile
from .AICondition import AICondition as _AICondition


class PlayerDetectedCondition(SubclassBaseFile):
    ResourceType = 0xDEC0CA0E
    ParentResourceType = _AICondition.ResourceType
    parent: _AICondition
