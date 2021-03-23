from pyUbiForge2.api.game import SubclassBaseFile
from .Component import Component as _Component


class VolumetricSoundComponent(SubclassBaseFile):
    ResourceType = 0x09734394
    ParentResourceType = _Component.ResourceType
    parent: _Component
