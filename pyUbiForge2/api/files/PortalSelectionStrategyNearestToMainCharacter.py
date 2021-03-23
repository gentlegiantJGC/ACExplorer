from pyUbiForge2.api.game import SubclassBaseFile
from .PortalSelectionStrategy import PortalSelectionStrategy as _PortalSelectionStrategy


class PortalSelectionStrategyNearestToMainCharacter(SubclassBaseFile):
    ResourceType = 0x96AD54B8
    ParentResourceType = _PortalSelectionStrategy.ResourceType
    parent: _PortalSelectionStrategy
