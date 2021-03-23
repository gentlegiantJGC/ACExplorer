from pyUbiForge2.api.game import SubclassBaseFile
from .DoneNode import DoneNode as _DoneNode


class ActionNode(SubclassBaseFile):
    ResourceType = 0xA1DF3794
    ParentResourceType = _DoneNode.ResourceType
    parent: _DoneNode
