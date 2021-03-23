from pyUbiForge2.api.game import SubclassBaseFile
from .Component import Component as _Component


class SoundBankEntityComponent(SubclassBaseFile):
    ResourceType = 0xDAB4219F
    ParentResourceType = _Component.ResourceType
    parent: _Component
