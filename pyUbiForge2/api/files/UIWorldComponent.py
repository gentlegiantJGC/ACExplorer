from pyUbiForge2.api.game import SubclassBaseFile
from .WorldComponent import WorldComponent as _WorldComponent


class UIWorldComponent(SubclassBaseFile):
    ResourceType = 0xEEC2D4C7
    ParentResourceType = _WorldComponent.ResourceType
    parent: _WorldComponent
