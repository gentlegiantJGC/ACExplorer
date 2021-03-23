from pyUbiForge2.api.game import SubclassBaseFile
from .BoneModifier import BoneModifier as _BoneModifier


class FollowBoneModifier(SubclassBaseFile):
    ResourceType = 0x13AE4B43
    ParentResourceType = _BoneModifier.ResourceType
    parent: _BoneModifier
