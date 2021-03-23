from pyUbiForge2.api.game import SubclassBaseFile
from .AICondition import AICondition as _AICondition


class LanguageCondition(SubclassBaseFile):
    ResourceType = 0x53E62540
    ParentResourceType = _AICondition.ResourceType
    parent: _AICondition
