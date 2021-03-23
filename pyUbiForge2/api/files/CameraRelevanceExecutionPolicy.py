from pyUbiForge2.api.game import SubclassBaseFile
from .IExecutionPolicy import IExecutionPolicy as _IExecutionPolicy


class CameraRelevanceExecutionPolicy(SubclassBaseFile):
    ResourceType = 0xC280CDB3
    ParentResourceType = _IExecutionPolicy.ResourceType
    parent: _IExecutionPolicy
