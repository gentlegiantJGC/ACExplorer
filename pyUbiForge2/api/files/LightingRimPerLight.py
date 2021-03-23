from pyUbiForge2.api.game import SubclassBaseFile
from .LightingOperator import LightingOperator as _LightingOperator


class LightingRimPerLight(SubclassBaseFile):
    ResourceType = 0x71E7D5D3
    ParentResourceType = _LightingOperator.ResourceType
    parent: _LightingOperator

