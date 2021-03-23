from pyUbiForge2.api.game import SubclassBaseFile
from .DampingMethod import DampingMethod as _DampingMethod


class AverageDampingMethod(SubclassBaseFile):
    ResourceType = 0x7FC40645
    ParentResourceType = _DampingMethod.ResourceType
    parent: _DampingMethod
