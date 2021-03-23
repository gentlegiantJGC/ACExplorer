from pyUbiForge2.api.game import SubclassBaseFile
from .ExplorationOffsetMethod import ExplorationOffsetMethod as _ExplorationOffsetMethod


class ExplorationOffsetEnhanceTargetDirectionMethod(SubclassBaseFile):
    ResourceType = 0x0A6FB7FB
    ParentResourceType = _ExplorationOffsetMethod.ResourceType
    parent: _ExplorationOffsetMethod
