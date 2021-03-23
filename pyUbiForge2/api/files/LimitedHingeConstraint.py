from pyUbiForge2.api.game import SubclassBaseFile
from .BaseHingeConstraint import BaseHingeConstraint as _BaseHingeConstraint


class LimitedHingeConstraint(SubclassBaseFile):
    ResourceType = 0xE1DD46AF
    ParentResourceType = _BaseHingeConstraint.ResourceType
    parent: _BaseHingeConstraint
