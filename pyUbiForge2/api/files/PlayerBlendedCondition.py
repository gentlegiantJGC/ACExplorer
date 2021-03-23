from pyUbiForge2.api.game import SubclassBaseFile
from .AICondition import AICondition as _AICondition


class PlayerBlendedCondition(SubclassBaseFile):
    ResourceType = 0x996E624C
    ParentResourceType = _AICondition.ResourceType
    parent: _AICondition
