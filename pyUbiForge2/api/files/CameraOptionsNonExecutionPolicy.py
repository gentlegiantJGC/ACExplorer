from pyUbiForge2.api.game import SubclassBaseFile
from .IExecutionPolicy import IExecutionPolicy as _IExecutionPolicy


class CameraOptionsNonExecutionPolicy(SubclassBaseFile):
    ResourceType = 0x46DE5F80
    ParentResourceType = _IExecutionPolicy.ResourceType
    parent: _IExecutionPolicy
