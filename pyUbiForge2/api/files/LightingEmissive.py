from pyUbiForge2.api.game import SubclassBaseFile
from .LightingOperator import LightingOperator as _LightingOperator


class LightingEmissive(SubclassBaseFile):
    ResourceType = 0x77164BF2
    ParentResourceType = _LightingOperator.ResourceType
    parent: _LightingOperator
