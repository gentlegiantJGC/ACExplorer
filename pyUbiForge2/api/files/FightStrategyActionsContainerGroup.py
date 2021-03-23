from pyUbiForge2.api.game import SubclassBaseFile
from .FightStrategyActionsContainer import (
    FightStrategyActionsContainer as _FightStrategyActionsContainer,
)


class FightStrategyActionsContainerGroup(SubclassBaseFile):
    ResourceType = 0x2A2EF75A
    ParentResourceType = _FightStrategyActionsContainer.ResourceType
    parent: _FightStrategyActionsContainer
