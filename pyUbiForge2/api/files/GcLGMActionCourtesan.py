from pyUbiForge2.api.game import SubclassBaseFile
from .GcLAbstractGroupManipulationAction import GcLAbstractGroupManipulationAction as _GcLAbstractGroupManipulationAction


class GcLGMActionCourtesan(SubclassBaseFile):
    ResourceType = 0x39B06627
    ParentResourceType = _GcLAbstractGroupManipulationAction.ResourceType
    parent: _GcLAbstractGroupManipulationAction

