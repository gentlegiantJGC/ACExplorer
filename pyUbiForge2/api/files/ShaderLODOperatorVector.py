from pyUbiForge2.api.game import SubclassBaseFile
from .ShaderLODOperator import ShaderLODOperator as _ShaderLODOperator


class ShaderLODOperatorVector(SubclassBaseFile):
    ResourceType = 0x20B22221
    ParentResourceType = _ShaderLODOperator.ResourceType
    parent: _ShaderLODOperator
