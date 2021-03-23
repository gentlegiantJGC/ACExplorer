from pyUbiForge2.api.game import SubclassBaseFile
from .GcLAbstractGroupManipulationFight import GcLAbstractGroupManipulationFight as _GcLAbstractGroupManipulationFight


class GcLGMFightMercenary(SubclassBaseFile):
    ResourceType = 0x3192F703
    ParentResourceType = _GcLAbstractGroupManipulationFight.ResourceType
    parent: _GcLAbstractGroupManipulationFight

