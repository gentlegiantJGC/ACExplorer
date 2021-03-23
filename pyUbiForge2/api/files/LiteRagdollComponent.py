from pyUbiForge2.api.game import SubclassBaseFile
from .Component import Component as _Component


class LiteRagdollComponent(SubclassBaseFile):
    ResourceType = 0x6CEC3B52
    ParentResourceType = _Component.ResourceType
    parent: _Component

