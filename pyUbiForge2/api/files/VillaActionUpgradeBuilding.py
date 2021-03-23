from pyUbiForge2.api.game import SubclassBaseFile
from .AIAction import AIAction as _AIAction


class VillaActionUpgradeBuilding(SubclassBaseFile):
    ResourceType = 0x4A4EC2F6
    ParentResourceType = _AIAction.ResourceType
    parent: _AIAction

