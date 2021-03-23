from pyUbiForge2.api.game import SubclassBaseFile
from .LightingOperator import LightingOperator as _LightingOperator


class LightingDiffuse(SubclassBaseFile):
    ResourceType = 0xF67EAA2B
    ParentResourceType = _LightingOperator.ResourceType
    parent: _LightingOperator
