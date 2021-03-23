from pyUbiForge2.api.game import SubclassBaseFile
from .GcLAbstractGroupManipulationAction import (
    GcLAbstractGroupManipulationAction as _GcLAbstractGroupManipulationAction,
)


class GcLGMActionMercenary(SubclassBaseFile):
    ResourceType = 0x1A80C4B5
    ParentResourceType = _GcLAbstractGroupManipulationAction.ResourceType
    parent: _GcLAbstractGroupManipulationAction
