from pyUbiForge2.api.game import SubclassBaseFile
from .Component import Component as _Component


class SiegeTrooper(SubclassBaseFile):
    ResourceType = 0x9749EAAD
    ParentResourceType = _Component.ResourceType
    parent: _Component
