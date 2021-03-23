from pyUbiForge2.api.game import SubclassBaseFile
from .Constraint import Constraint as _Constraint


class BallAndSocketConstraint(SubclassBaseFile):
    ResourceType = 0x86C2BFF9
    ParentResourceType = _Constraint.ResourceType
    parent: _Constraint

