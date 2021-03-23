from pyUbiForge2.api.game import SubclassBaseFile
from .GcLAbstractGroupManipulationEmbedded import GcLAbstractGroupManipulationEmbedded as _GcLAbstractGroupManipulationEmbedded


class GcLGMFollowAbilityCourtesan(SubclassBaseFile):
    ResourceType = 0x389E1AF3
    ParentResourceType = _GcLAbstractGroupManipulationEmbedded.ResourceType
    parent: _GcLAbstractGroupManipulationEmbedded

