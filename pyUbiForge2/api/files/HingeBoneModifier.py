from pyUbiForge2.api.game import SubclassBaseFile
from .BoneModifier import BoneModifier as _BoneModifier


class HingeBoneModifier(SubclassBaseFile):
    ResourceType = 0x324796C7
    ParentResourceType = _BoneModifier.ResourceType
    parent: _BoneModifier

