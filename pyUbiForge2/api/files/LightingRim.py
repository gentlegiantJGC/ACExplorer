from pyUbiForge2.api.game import SubclassBaseFile
from .LightingOperator import LightingOperator as _LightingOperator


class LightingRim(SubclassBaseFile):
    ResourceType = 0xFE00D9F4
    ParentResourceType = _LightingOperator.ResourceType
    parent: _LightingOperator
