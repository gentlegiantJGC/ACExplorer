from pyUbiForge2.api.game import SubclassBaseFile
from .GcLAbstractGroupManipulationEmbedded import (
    GcLAbstractGroupManipulationEmbedded as _GcLAbstractGroupManipulationEmbedded,
)


class GcLAbstractGroupManipulationAction(SubclassBaseFile):
    ResourceType = 0xE1C14FF0
    ParentResourceType = _GcLAbstractGroupManipulationEmbedded.ResourceType
    parent: _GcLAbstractGroupManipulationEmbedded
