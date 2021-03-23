from pyUbiForge2.api.game import SubclassBaseFile
from .LightingOperator import LightingOperator as _LightingOperator


class LightingHairAnisotropic(SubclassBaseFile):
    ResourceType = 0x3D1CA8BD
    ParentResourceType = _LightingOperator.ResourceType
    parent: _LightingOperator
