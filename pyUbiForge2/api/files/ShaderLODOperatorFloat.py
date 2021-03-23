from pyUbiForge2.api.game import SubclassBaseFile
from .ShaderLODOperator import ShaderLODOperator as _ShaderLODOperator


class ShaderLODOperatorFloat(SubclassBaseFile):
    ResourceType = 0x7BEFECB5
    ParentResourceType = _ShaderLODOperator.ResourceType
    parent: _ShaderLODOperator

