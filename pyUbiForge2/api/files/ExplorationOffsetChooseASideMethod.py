from pyUbiForge2.api.game import SubclassBaseFile
from .ExplorationOffsetMethod import ExplorationOffsetMethod as _ExplorationOffsetMethod


class ExplorationOffsetChooseASideMethod(SubclassBaseFile):
    ResourceType = 0xF0C7D826
    ParentResourceType = _ExplorationOffsetMethod.ResourceType
    parent: _ExplorationOffsetMethod
