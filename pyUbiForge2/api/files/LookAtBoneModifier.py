from pyUbiForge2.api.game import SubclassBaseFile
from .BoneModifier import BoneModifier as _BoneModifier


class LookAtBoneModifier(SubclassBaseFile):
    ResourceType = 0x08D774B2
    ParentResourceType = _BoneModifier.ResourceType
    parent: _BoneModifier

