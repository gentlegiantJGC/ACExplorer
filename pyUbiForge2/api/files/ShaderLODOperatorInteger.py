from pyUbiForge2.api.game import SubclassBaseFile
from .ShaderLODOperator import ShaderLODOperator as _ShaderLODOperator


class ShaderLODOperatorInteger(SubclassBaseFile):
    ResourceType = 0xEAE4EF43
    ParentResourceType = _ShaderLODOperator.ResourceType
    parent: _ShaderLODOperator
