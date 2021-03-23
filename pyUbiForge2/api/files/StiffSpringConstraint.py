from pyUbiForge2.api.game import SubclassBaseFile
from .Constraint import Constraint as _Constraint


class StiffSpringConstraint(SubclassBaseFile):
    ResourceType = 0xC422E3BB
    ParentResourceType = _Constraint.ResourceType
    parent: _Constraint
