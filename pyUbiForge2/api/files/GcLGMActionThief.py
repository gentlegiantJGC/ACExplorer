from pyUbiForge2.api.game import SubclassBaseFile
from .GcLAbstractGroupManipulationAction import (
    GcLAbstractGroupManipulationAction as _GcLAbstractGroupManipulationAction,
)


class GcLGMActionThief(SubclassBaseFile):
    ResourceType = 0xA1A03285
    ParentResourceType = _GcLAbstractGroupManipulationAction.ResourceType
    parent: _GcLAbstractGroupManipulationAction
