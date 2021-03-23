from pyUbiForge2.api.game import SubclassBaseFile
from .Node import Node as _Node


class DoneNode(SubclassBaseFile):
    ResourceType = 0x8E343DFD
    ParentResourceType = _Node.ResourceType
    parent: _Node

