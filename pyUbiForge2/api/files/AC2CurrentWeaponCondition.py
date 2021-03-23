from pyUbiForge2.api.game import SubclassBaseFile
from .IRuleCondition import IRuleCondition as _IRuleCondition


class AC2CurrentWeaponCondition(SubclassBaseFile):
    ResourceType = 0x3D46CF4D
    ParentResourceType = _IRuleCondition.ResourceType
    parent: _IRuleCondition

