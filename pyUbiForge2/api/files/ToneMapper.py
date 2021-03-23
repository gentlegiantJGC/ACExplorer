from pyUbiForge2.api.game import SubclassBaseFile
from .PostEffect import PostEffect as _PostEffect


class ToneMapper(SubclassBaseFile):
    ResourceType = 0x429BD18B
    ParentResourceType = _PostEffect.ResourceType
    parent: _PostEffect
