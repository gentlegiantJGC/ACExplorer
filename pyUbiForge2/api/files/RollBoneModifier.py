from pyUbiForge2.api.game import SubclassBaseFile
from .BoneModifier import BoneModifier as _BoneModifier


class RollBoneModifier(SubclassBaseFile):
    ResourceType = 0x76D082F6
    ParentResourceType = _BoneModifier.ResourceType
    parent: _BoneModifier
