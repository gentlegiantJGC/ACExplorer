from pyUbiForge2.api.game import SubclassBaseFile
from .ProgressionDampingMethod import ProgressionDampingMethod as _ProgressionDampingMethod


class TimeDampingMethod(SubclassBaseFile):
    ResourceType = 0x92C9931C
    ParentResourceType = _ProgressionDampingMethod.ResourceType
    parent: _ProgressionDampingMethod

