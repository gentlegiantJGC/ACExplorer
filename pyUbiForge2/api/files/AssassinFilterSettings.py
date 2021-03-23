from pyUbiForge2.api.game import SubclassBaseFile
from .PostEffect import PostEffect as _PostEffect


class AssassinFilterSettings(SubclassBaseFile):
    ResourceType = 0x661A55D1
    ParentResourceType = _PostEffect.ResourceType
    parent: _PostEffect

