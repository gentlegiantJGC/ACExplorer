from pyUbiForge2.api.game import SubclassBaseFile
from .AICondition import AICondition as _AICondition


class LifeCondition(SubclassBaseFile):
    ResourceType = 0xCB39B54A
    ParentResourceType = _AICondition.ResourceType
    parent: _AICondition
