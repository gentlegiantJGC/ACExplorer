from pyUbiForge2.api.game import SubclassBaseFile
from .ExecutionSet import ExecutionSet as _ExecutionSet


class SelectiveExecutionSet(SubclassBaseFile):
    ResourceType = 0x9B1EC562
    ParentResourceType = _ExecutionSet.ResourceType
    parent: _ExecutionSet

