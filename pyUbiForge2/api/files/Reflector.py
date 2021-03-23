from pyUbiForge2.api.game import SubclassBaseFile
from .VisualComponent import VisualComponent as _VisualComponent


class Reflector(SubclassBaseFile):
    ResourceType = 0xC221625B
    ParentResourceType = _VisualComponent.ResourceType
    parent: _VisualComponent
