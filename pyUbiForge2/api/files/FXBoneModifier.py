from pyUbiForge2.api.game import SubclassBaseFile
from .BoneModifier import BoneModifier as _BoneModifier


class FXBoneModifier(SubclassBaseFile):
    ResourceType = 0xCA0CFEE7
    ParentResourceType = _BoneModifier.ResourceType
    parent: _BoneModifier
