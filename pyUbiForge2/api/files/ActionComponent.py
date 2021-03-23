from pyUbiForge2.api.game import SubclassBaseFile
from .Component import Component as _Component


class ActionComponent(SubclassBaseFile):
    ResourceType = 0xBADD286C
    ParentResourceType = _Component.ResourceType
    parent: _Component
