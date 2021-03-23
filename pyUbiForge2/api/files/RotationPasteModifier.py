from pyUbiForge2.api.game import SubclassBaseFile
from .BoneModifier import BoneModifier as _BoneModifier


class RotationPasteModifier(SubclassBaseFile):
    ResourceType = 0x711759AF
    ParentResourceType = _BoneModifier.ResourceType
    parent: _BoneModifier

