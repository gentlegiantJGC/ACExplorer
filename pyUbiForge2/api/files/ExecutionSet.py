from pyUbiForge2.api.game import SubclassBaseFile
from .IExecution import IExecution as _IExecution


class ExecutionSet(SubclassBaseFile):
    ResourceType = 0xF73B28B0
    ParentResourceType = _IExecution.ResourceType
    parent: _IExecution

