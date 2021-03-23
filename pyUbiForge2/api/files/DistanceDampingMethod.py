from pyUbiForge2.api.game import SubclassBaseFile
from .ProgressionDampingMethod import ProgressionDampingMethod as _ProgressionDampingMethod


class DistanceDampingMethod(SubclassBaseFile):
    ResourceType = 0xEF0C3053
    ParentResourceType = _ProgressionDampingMethod.ResourceType
    parent: _ProgressionDampingMethod

