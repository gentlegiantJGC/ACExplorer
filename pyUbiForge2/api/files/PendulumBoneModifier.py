from pyUbiForge2.api.game import SubclassBaseFile
from .BoneModifier import BoneModifier as _BoneModifier


class PendulumBoneModifier(SubclassBaseFile):
    ResourceType = 0x0544175B
    ParentResourceType = _BoneModifier.ResourceType
    parent: _BoneModifier

