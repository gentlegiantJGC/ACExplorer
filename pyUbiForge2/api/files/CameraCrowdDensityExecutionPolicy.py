from pyUbiForge2.api.game import SubclassBaseFile
from .IExecutionPolicy import IExecutionPolicy as _IExecutionPolicy


class CameraCrowdDensityExecutionPolicy(SubclassBaseFile):
    ResourceType = 0xF0E41576
    ParentResourceType = _IExecutionPolicy.ResourceType
    parent: _IExecutionPolicy

