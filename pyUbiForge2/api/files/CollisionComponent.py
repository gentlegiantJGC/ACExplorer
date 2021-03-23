from pyUbiForge2.api.game import SubclassBaseFile
from .Component import Component as _Component


class CollisionComponent(SubclassBaseFile):
    ResourceType = 0xAA95E301
    ParentResourceType = _Component.ResourceType
    parent: _Component
