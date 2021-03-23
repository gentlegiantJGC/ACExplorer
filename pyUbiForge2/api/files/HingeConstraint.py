from pyUbiForge2.api.game import SubclassBaseFile
from .BaseHingeConstraint import BaseHingeConstraint as _BaseHingeConstraint


class HingeConstraint(SubclassBaseFile):
    ResourceType = 0xECEB4833
    ParentResourceType = _BaseHingeConstraint.ResourceType
    parent: _BaseHingeConstraint

