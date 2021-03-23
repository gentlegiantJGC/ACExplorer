from pyUbiForge2.api.game import SubclassBaseFile
from .GcLAbstractGroupManipulationFight import (
    GcLAbstractGroupManipulationFight as _GcLAbstractGroupManipulationFight,
)


class GcLGMFightThief(SubclassBaseFile):
    ResourceType = 0x5179469D
    ParentResourceType = _GcLAbstractGroupManipulationFight.ResourceType
    parent: _GcLAbstractGroupManipulationFight
