from pyUbiForge2.api.game import SubclassBaseFile
from .DoneNode import DoneNode as _DoneNode


class ActionDispatcher(SubclassBaseFile):
    ResourceType = 0x3FA6BD83
    ParentResourceType = _DoneNode.ResourceType
    parent: _DoneNode

