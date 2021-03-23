from pyUbiForge2.api.game import SubclassBaseFile
from .Constraint import Constraint as _Constraint


class RagdollConstraint(SubclassBaseFile):
    ResourceType = 0x472B0467
    ParentResourceType = _Constraint.ResourceType
    parent: _Constraint

