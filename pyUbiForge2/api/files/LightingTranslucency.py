from pyUbiForge2.api.game import SubclassBaseFile
from .LightingOperator import LightingOperator as _LightingOperator


class LightingTranslucency(SubclassBaseFile):
    ResourceType = 0x35A2FE5B
    ParentResourceType = _LightingOperator.ResourceType
    parent: _LightingOperator

