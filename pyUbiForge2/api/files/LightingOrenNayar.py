from pyUbiForge2.api.game import SubclassBaseFile
from .LightingOperator import LightingOperator as _LightingOperator


class LightingOrenNayar(SubclassBaseFile):
    ResourceType = 0x84A57E2F
    ParentResourceType = _LightingOperator.ResourceType
    parent: _LightingOperator

