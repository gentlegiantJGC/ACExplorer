from pyUbiForge2.api.game import SubclassBaseFile
from .FightStrategyActionsContainer import FightStrategyActionsContainer as _FightStrategyActionsContainer


class FightStrategyActionsContainerSingle(SubclassBaseFile):
    ResourceType = 0xAA50477F
    ParentResourceType = _FightStrategyActionsContainer.ResourceType
    parent: _FightStrategyActionsContainer

