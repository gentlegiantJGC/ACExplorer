from pyUbiForge2.api.game import SubclassBaseFile
from .GcLAbstractGroupManipulationFight import GcLAbstractGroupManipulationFight as _GcLAbstractGroupManipulationFight


class GcLGMFightCourtesan(SubclassBaseFile):
    ResourceType = 0x12A25591
    ParentResourceType = _GcLAbstractGroupManipulationFight.ResourceType
    parent: _GcLAbstractGroupManipulationFight

