from pyUbiForge2.api.game import SubclassBaseFile
from .IExecutionPolicy import IExecutionPolicy as _IExecutionPolicy


class CameraTargetFacingExecutionPolicy(SubclassBaseFile):
    ResourceType = 0xABC90F63
    ParentResourceType = _IExecutionPolicy.ResourceType
    parent: _IExecutionPolicy

