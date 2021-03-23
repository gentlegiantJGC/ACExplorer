from pyUbiForge2.api.game import SubclassBaseFile
from .PostEffect import PostEffect as _PostEffect


class BlurredMaskSettings(SubclassBaseFile):
    ResourceType = 0x3D7BDF26
    ParentResourceType = _PostEffect.ResourceType
    parent: _PostEffect
