from pyUbiForge2.api.game import SubclassBaseFile
from .BoneModifier import BoneModifier as _BoneModifier


class SpringBoxModifier(SubclassBaseFile):
    ResourceType = 0xF9D25748
    ParentResourceType = _BoneModifier.ResourceType
    parent: _BoneModifier
