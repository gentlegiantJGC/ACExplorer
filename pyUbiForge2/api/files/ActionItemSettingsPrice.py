from pyUbiForge2.api.game import SubclassBaseFile
from .AIAction import AIAction as _AIAction


class ActionItemSettingsPrice(SubclassBaseFile):
    ResourceType = 0x5F355273
    ParentResourceType = _AIAction.ResourceType
    parent: _AIAction