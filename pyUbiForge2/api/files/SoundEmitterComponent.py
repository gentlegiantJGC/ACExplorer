from pyUbiForge2.api.game import SubclassBaseFile
from .Component import Component as _Component


class SoundEmitterComponent(SubclassBaseFile):
    ResourceType = 0x056F86AB
    ParentResourceType = _Component.ResourceType
    parent: _Component
