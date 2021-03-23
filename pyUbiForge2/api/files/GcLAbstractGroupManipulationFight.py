from pyUbiForge2.api.game import SubclassBaseFile
from .GcLAbstractGroupManipulationEmbedded import (
    GcLAbstractGroupManipulationEmbedded as _GcLAbstractGroupManipulationEmbedded,
)


class GcLAbstractGroupManipulationFight(SubclassBaseFile):
    ResourceType = 0x903E41F3
    ParentResourceType = _GcLAbstractGroupManipulationEmbedded.ResourceType
    parent: _GcLAbstractGroupManipulationEmbedded
