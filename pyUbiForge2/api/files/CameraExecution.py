from pyUbiForge2.api.game import SubclassBaseFile
from .IExecution import IExecution as _IExecution


class CameraExecution(SubclassBaseFile):
    ResourceType = 0x1A9A18CF
    ParentResourceType = _IExecution.ResourceType
    parent: _IExecution
