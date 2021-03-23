from pyUbiForge2.api.game import SubclassBaseFile
from .BoneModifier import BoneModifier as _BoneModifier


class RotationConstraintModifier(SubclassBaseFile):
    ResourceType = 0xA2A0524C
    ParentResourceType = _BoneModifier.ResourceType
    parent: _BoneModifier
