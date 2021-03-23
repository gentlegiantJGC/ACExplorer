from pyUbiForge2.api.game import SubclassBaseFile
from .Component import Component as _Component


class RopeComponent(SubclassBaseFile):
    ResourceType = 0xD88E9D5C
    ParentResourceType = _Component.ResourceType
    parent: _Component
