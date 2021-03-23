from pyUbiForge2.api.game import SubclassBaseFile
from .Constraint import Constraint as _Constraint


class BaseHingeConstraint(SubclassBaseFile):
    ResourceType = 0xA423D3B5
    ParentResourceType = _Constraint.ResourceType
    parent: _Constraint
