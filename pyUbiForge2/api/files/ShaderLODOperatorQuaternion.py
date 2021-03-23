from pyUbiForge2.api.game import SubclassBaseFile
from .ShaderLODOperator import ShaderLODOperator as _ShaderLODOperator


class ShaderLODOperatorQuaternion(SubclassBaseFile):
    ResourceType = 0x96AC5F80
    ParentResourceType = _ShaderLODOperator.ResourceType
    parent: _ShaderLODOperator
