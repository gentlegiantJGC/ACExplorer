from pyUbiForge2.api.game import SubclassBaseFile
from .WorldComponent import WorldComponent as _WorldComponent


class DebugSettings(SubclassBaseFile):
    ResourceType = 0x9B7A3615
    ParentResourceType = _WorldComponent.ResourceType
    parent: _WorldComponent

