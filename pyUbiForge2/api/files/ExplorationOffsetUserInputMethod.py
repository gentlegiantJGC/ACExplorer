from pyUbiForge2.api.game import SubclassBaseFile
from .ExplorationOffsetMethod import ExplorationOffsetMethod as _ExplorationOffsetMethod


class ExplorationOffsetUserInputMethod(SubclassBaseFile):
    ResourceType = 0x298D8D2C
    ParentResourceType = _ExplorationOffsetMethod.ResourceType
    parent: _ExplorationOffsetMethod

