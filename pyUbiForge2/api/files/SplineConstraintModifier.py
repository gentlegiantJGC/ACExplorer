from pyUbiForge2.api.game import SubclassBaseFile
from .BoneModifier import BoneModifier as _BoneModifier


class SplineConstraintModifier(SubclassBaseFile):
    ResourceType = 0xB6FC82EE
    ParentResourceType = _BoneModifier.ResourceType
    parent: _BoneModifier
