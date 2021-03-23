from pyUbiForge2.api.game import SubclassBaseFile
from .IExecutionPolicy import IExecutionPolicy as _IExecutionPolicy


class CameraProximityExecutionPolicy(SubclassBaseFile):
    ResourceType = 0x5D45E7C6
    ParentResourceType = _IExecutionPolicy.ResourceType
    parent: _IExecutionPolicy
