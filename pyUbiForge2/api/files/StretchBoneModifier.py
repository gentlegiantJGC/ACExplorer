from pyUbiForge2.api.game import SubclassBaseFile
from .BoneModifier import BoneModifier as _BoneModifier


class StretchBoneModifier(SubclassBaseFile):
    ResourceType = 0xCF6D16FA
    ParentResourceType = _BoneModifier.ResourceType
    parent: _BoneModifier

