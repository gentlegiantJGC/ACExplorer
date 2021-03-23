from pyUbiForge2.api.game import SubclassBaseFile
from .AICondition import AICondition as _AICondition


class PlayerKillTargetWeaponCondition(SubclassBaseFile):
    ResourceType = 0x0529F53D
    ParentResourceType = _AICondition.ResourceType
    parent: _AICondition

