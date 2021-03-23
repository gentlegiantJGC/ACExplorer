from pyUbiForge2.api.game import SubclassBaseFile
from .LightingOperator import LightingOperator as _LightingOperator


class LightingSpecular(SubclassBaseFile):
    ResourceType = 0x791945CF
    ParentResourceType = _LightingOperator.ResourceType
    parent: _LightingOperator
