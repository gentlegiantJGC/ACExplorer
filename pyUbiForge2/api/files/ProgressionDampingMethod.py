from pyUbiForge2.api.game import SubclassBaseFile
from .DampingMethod import DampingMethod as _DampingMethod


class ProgressionDampingMethod(SubclassBaseFile):
    ResourceType = 0x44759DE4
    ParentResourceType = _DampingMethod.ResourceType
    parent: _DampingMethod

