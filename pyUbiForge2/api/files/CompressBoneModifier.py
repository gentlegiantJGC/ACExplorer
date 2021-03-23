from pyUbiForge2.api.game import SubclassBaseFile
from .BoneModifier import BoneModifier as _BoneModifier


class CompressBoneModifier(SubclassBaseFile):
    ResourceType = 0x844987D6
    ParentResourceType = _BoneModifier.ResourceType
    parent: _BoneModifier
